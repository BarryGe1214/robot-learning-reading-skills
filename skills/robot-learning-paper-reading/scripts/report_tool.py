#!/usr/bin/env python3
"""Build/check an offline illustrated reading. Python 3.10+, standard library only.

Input HTML is deliberately restricted; use native MathML for equations. This
checks artifact structure, not scientific correctness, rights or visual quality.
"""
import argparse
import base64
import binascii
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET


class ReportError(ValueError):
    pass


TEXT_TAGS = set("p br strong em b i sub sup code pre blockquote ul ol li table thead tbody tr th td a span div h3 h4".split())
MATH_TAGS = set("math mrow mi mn mo mtext mspace ms mfrac msqrt mroot msub msup msubsup mover munder munderover mfenced mtable mtr mtd mstyle mpadded mphantom menclose".split())
DOC_TAGS = set("html head meta title style body header main section h1 h2 figure img figcaption footer".split())
VOID = {"br", "img", "meta", "mspace"}
ATTRS = {"class", "id", "title", "lang", "colspan", "rowspan"}
MATH_ATTRS = {"xmlns", "display", "mathvariant", "stretchy", "fence", "separator", "accent", "accentunder", "form", "lspace", "rspace", "displaystyle", "scriptlevel", "linethickness", "rowalign", "columnalign", "columnspacing", "rowspacing", "width", "height", "depth", "notation", "open", "close", "separators"}
STYLE = """body{font-family:system-ui,sans-serif;color:#172b3b;background:#f7f8fa;margin:0;line-height:1.8}main{max-width:1020px;margin:auto;padding:40px 24px}header,section{background:white;border:1px solid #dce3e8;border-radius:12px;padding:24px;margin-bottom:22px}h1{line-height:1.35}h2{color:#184e67}img{max-width:100%;height:auto;display:block;margin:auto}figure{margin:24px 0}figcaption,.meta{font-size:.92rem;color:#415767}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccd7de;padding:8px}blockquote{border-left:4px solid #87a8bb;padding-left:16px;margin-left:0}math[display=block]{overflow-x:auto;margin:18px 0}code{white-space:pre-wrap}a{color:#126782}@media print{body{background:white}main{padding:0}section{break-inside:auto}figure{break-inside:avoid}}"""


def required(obj, key, context):
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ReportError(f"{context}.{key} must be a nonempty string")
    if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b|待填|待补充", value, re.I):
        raise ReportError(f"Unfinished placeholder in {context}.{key}")
    return value.strip()


def public_link(value):
    parts = urlsplit(value)
    return parts.scheme in {"https", "http"} and bool(parts.netloc) and not parts.username and not parts.password


def image_bytes(data, mime):
    if mime == "image/png":
        if not data.startswith(b"\x89PNG\r\n\x1a\n") or b"IEND" not in data[-12:]:
            raise ReportError("Invalid PNG signature/end marker")
    elif mime == "image/jpeg":
        if not data.startswith(b"\xff\xd8") or not data.endswith(b"\xff\xd9"):
            raise ReportError("Invalid JPEG signature/end marker")
    elif mime == "image/svg+xml":
        try:
            root = ET.fromstring(data)
        except ET.ParseError as exc:
            raise ReportError(f"Invalid SVG XML: {exc}") from exc
        if root.tag.split("}")[-1] != "svg":
            raise ReportError("SVG root missing")
        for element in root.iter():
            if element.tag.split("}")[-1].lower() in {"script", "foreignobject", "image", "use", "style", "a", "animate", "animatetransform", "set"}:
                raise ReportError("SVG contains active or linked content")
            for key, value in element.attrib.items():
                name = key.split("}")[-1].lower()
                if name.startswith("on") or name in {"href", "style"} or re.search(r"url\s*\(", value, re.I):
                    raise ReportError("SVG contains active or external attributes")
    else:
        raise ReportError("Only PNG, JPEG and passive SVG are supported")


def embedded_image(src):
    match = re.fullmatch(r"data:(image/(?:png|jpeg|svg\+xml));base64,([A-Za-z0-9+/=\s]+)", src)
    if not match:
        raise ReportError("Image must be embedded as base64 PNG/JPEG/SVG")
    try:
        data = base64.b64decode(re.sub(r"\s", "", match[2]), validate=True)
    except binascii.Error as exc:
        raise ReportError("Invalid image base64") from exc
    image_bytes(data, match[1])


class Inspector(HTMLParser):
    def __init__(self, document=False):
        super().__init__(convert_charrefs=True)
        self.document = document
        self.stack = []
        self.images = 0
        self.captions = 0
        self.math = 0
        self.meta = {}
        self.style = []
        self.figure = None

    def handle_starttag(self, tag, attrs):
        allowed = TEXT_TAGS | MATH_TAGS | (DOC_TAGS if self.document else set())
        if tag not in allowed:
            raise ReportError(f"Unsupported HTML tag: {tag}")
        values = dict(attrs)
        if len(values) != len(attrs):
            raise ReportError(f"Duplicate attribute on {tag}")
        for key, value in attrs:
            permitted = ATTRS | (MATH_ATTRS if tag in MATH_TAGS else set())
            if tag == "a":
                permitted |= {"href"}
            if tag == "img":
                permitted |= {"src", "alt"}
            if tag == "meta":
                permitted |= {"name", "content", "charset"}
            if key not in permitted or value is None:
                raise ReportError(f"Unsupported attribute: {tag}.{key}")
        if tag == "a" and not (public_link(values.get("href", "")) or values.get("href", "").startswith("#")):
            raise ReportError("Links must be http(s) citations or same-document anchors")
        if tag == "figure":
            if self.figure is not None:
                raise ReportError("Nested figures are unsupported")
            self.figure = {"images": 0, "captions": 0, "caption_text": ""}
        if tag == "img":
            if "figure" not in self.stack or not values.get("alt", "").strip():
                raise ReportError("Image requires a figure and nonempty alt text")
            embedded_image(values.get("src", ""))
            self.images += 1
            self.figure["images"] += 1
        if tag == "figcaption":
            if "figure" not in self.stack:
                raise ReportError("Caption outside figure")
            self.captions += 1
            self.figure["captions"] += 1
        if tag == "math":
            self.math += 1
        if tag == "meta" and "name" in values:
            self.meta[values["name"]] = values.get("content", "")
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID or not self.stack or self.stack[-1] != tag:
            raise ReportError(f"Unbalanced HTML closing tag: {tag}")
        if tag == "figure":
            if self.figure["images"] != 1 or self.figure["captions"] != 1 or not self.figure["caption_text"].strip():
                raise ReportError("Each figure requires exactly one image and one nonempty caption")
            self.figure = None
        self.stack.pop()

    def handle_data(self, data):
        if self.figure is not None and "figcaption" in self.stack:
            self.figure["caption_text"] += data
        if "style" in self.stack:
            self.style.append(data)
        elif re.search(r"\\[\[(]|\\(?:frac|hat|mathrm|begin|alpha|theta)\b", data):
            raise ReportError("Unrendered LaTeX found; provide native MathML or an equation image")
        if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b|待填|待补充", data, re.I):
            raise ReportError("Unfinished placeholder in HTML")

    def finish(self):
        self.close()
        if self.stack:
            raise ReportError(f"Unclosed HTML tags: {self.stack}")
        if self.document and "".join(self.style) != STYLE:
            raise ReportError("Unexpected stylesheet; use the generated standalone template")


def fragment(value, context):
    if not isinstance(value, str) or not value.strip():
        raise ReportError(f"{context} must contain HTML")
    parser = Inspector()
    parser.feed(value)
    parser.finish()
    return value


def check_html(text):
    parser = Inspector(document=True)
    parser.feed(text)
    parser.finish()
    for key in ("paper-id", "paper-version", "skill-version", "skill-revision"):
        if not parser.meta.get(key, "").strip():
            raise ReportError(f"Missing report metadata: {key}")
    if parser.images != parser.captions:
        raise ReportError("Image/caption count mismatch")
    count = parser.meta.get("expected-image-count", "")
    illustrated = parser.meta.get("illustrated", "")
    if not count.isdigit() or illustrated not in {"true", "false"}:
        raise ReportError("Missing/invalid expected-image-count or illustrated metadata")
    if parser.images != int(count):
        raise ReportError("Embedded image count differs from the declared delivery contract")
    if illustrated == "true" and parser.images == 0:
        raise ReportError("Illustrated report has no images")
    for item in re.findall(r"<math\b.*?</math>", text, re.S):
        try:
            ET.fromstring(item)
        except ET.ParseError as exc:
            raise ReportError(f"Invalid MathML XML: {exc}") from exc
    return {"status": "pass", "embedded_images": parser.images, "mathml_blocks": parser.math,
            "external_asset_dependencies": 0, "visual_inspection": "not_run",
            "scientific_accuracy": "not_checked", "reuse_permission": "not_checked"}


def build(manifest_path, output):
    manifest_path = Path(manifest_path).resolve()
    spec = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    input_paths = {manifest_path}
    title = required(spec, "title", "report")
    paper = spec.get("paper", {})
    skill = spec.get("skill", {})
    fields = {
        "paper-id": required(paper, "id", "paper"),
        "paper-version": required(paper, "version", "paper"),
        "skill-version": required(skill, "version", "skill"),
        "skill-revision": required(skill, "revision", "skill"),
    }
    url = paper.get("url")
    if url and not public_link(url):
        raise ReportError("paper.url must be an http(s) citation")
    scope = required(spec, "source_scope", "report")
    sections = spec.get("sections")
    if not isinstance(sections, list) or not sections:
        raise ReportError("sections must be a nonempty list")
    esc = html.escape
    body = []
    total_images = 0
    for index, section in enumerate(sections, 1):
        ctx = f"sections[{index}]"
        body.append(f'<section><h2>{esc(required(section, "heading", ctx))}</h2>')
        body.append(fragment(section.get("html"), ctx + ".html"))
        figures = section.get("figures", [])
        if not isinstance(figures, list):
            raise ReportError(ctx + ".figures must be a list")
        for number, figure in enumerate(figures, 1):
            fctx = f"{ctx}.figures[{number}]"
            asset = (manifest_path.parent / required(figure, "path", fctx)).resolve()
            input_paths.add(asset)
            if not asset.is_file():
                raise ReportError(f"Missing image: {asset}")
            mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml"}.get(asset.suffix.lower())
            raw = asset.read_bytes()
            image_bytes(raw, mime)
            alt = required(figure, "alt", fctx)
            caption = required(figure, "caption", fctx)
            source = required(figure, "source", fctx)
            page = figure.get("page")
            if not isinstance(page, int) or isinstance(page, bool) or page < 1:
                raise ReportError(fctx + ".page must be a positive, 1-based PDF page number")
            kind = required(figure, "kind", fctx)
            if kind not in {"original", "reconstructed", "teaching"}:
                raise ReportError(fctx + ".kind must be original, reconstructed or teaching")
            explanation = fragment(figure.get("explanation_html"), fctx + ".explanation_html")
            encoded = base64.b64encode(raw).decode("ascii")
            body.append(f'<figure><img src="data:{mime};base64,{encoded}" alt="{esc(alt)}"><figcaption>{esc(caption)} — {esc(source)}, PDF p. {page}; {esc(kind)}.</figcaption>{explanation}</figure>')
            total_images += 1
        body.append("</section>")
    if spec.get("illustrated", True) and total_images == 0:
        raise ReportError("Illustrated report has no images; set illustrated=false only for an intentional text-only report")
    if not isinstance(spec.get("illustrated", True), bool):
        raise ReportError("illustrated must be a JSON boolean")
    fields["expected-image-count"] = str(total_images)
    fields["illustrated"] = str(spec.get("illustrated", True)).lower()
    meta = "".join(f'<meta name="{key}" content="{esc(value)}">' for key, value in fields.items())
    source_link = f'<a href="{esc(url)}">{esc(fields["paper-id"])}</a>' if url else esc(fields["paper-id"])
    report = f'<!doctype html><html lang="{esc(spec.get("language", "zh-CN"))}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{meta}<title>{esc(title)}</title><style>{STYLE}</style></head><body><main><header><h1>{esc(title)}</h1><p class="meta">{source_link} · {esc(fields["paper-version"])}<br>Skill {esc(fields["skill-version"])} · {esc(fields["skill-revision"])}</p><p class="meta">{esc(scope)}</p></header>{"".join(body)}</main></body></html>'
    result = check_html(report)
    target = Path(output).resolve()
    if target in input_paths:
        raise ReportError("Output must not overwrite the manifest or an input image")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(report, encoding="utf-8")
    result["output"] = str(target)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build_cmd = commands.add_parser("build", help="Build and mechanically check a standalone report")
    build_cmd.add_argument("manifest")
    build_cmd.add_argument("output")
    check_cmd = commands.add_parser("check", help="Check an HTML report produced by this helper")
    check_cmd.add_argument("report")
    args = parser.parse_args()
    try:
        result = build(args.manifest, args.output) if args.command == "build" else check_html(Path(args.report).read_text(encoding="utf-8"))
    except (ReportError, OSError, ValueError, TypeError, AttributeError) as exc:
        print(json.dumps({"status": "fail", "error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
