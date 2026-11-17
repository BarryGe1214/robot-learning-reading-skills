# Standalone illustrated report helper

Use this only when a file deliverable is useful or requested. The helper supplies repeatable HTML assembly and mechanical checks; the agent still reads the paper, selects and inspects crops, writes the explanation, and renders the final file.

## Local workflow

1. Obtain the exact authorized PDF and render/crop the decisive figures using available PDF tools. Follow [figure-extraction](figure-extraction.md); inspect each actual crop. Do not install a PDF library as a hidden prerequisite.
2. Write a UTF-8 JSON manifest beside the working crops, outside the public skill repository. Preserve the paper identifier/version, accessible source scope and actual skill revision. Use `unknown` when metadata cannot be verified; do not invent it.
3. Run Python 3.10+ with explicit input and output paths:

```text
python /path/to/skill/scripts/report_tool.py build /work/report.json /work/report.html
python /path/to/skill/scripts/report_tool.py check /work/report.html
```

The helper uses only the Python standard library, performs no network requests, and installs nothing. Resolve the interpreter through the host's available runtime; the command `python` is illustrative. Image paths are relative to the manifest unless absolute. The output contains embedded PNG, JPEG or passive SVG assets and native MathML; it needs no external fonts, JavaScript, stylesheet or math CDN. Source citation links remain clickable and are not rendering dependencies.

4. Open the final HTML in the actual delivery environment. Inspect image loading, crop boundaries, legends, mathematical layout and reading order. Read the rendered report as a guide: problem → intuition → mechanism → evidence. Fix failures before delivery.
5. Save the artifact using the host's authorized file route. Verify availability separately. Include an original crop and explanation in the conversation when required and supported. A successful build does not prove that a user received the file or saw inline images.

## Manifest contract

The following is synthetic teaching material, not a paper result. Replace its source information and content with verified task inputs. Do not execute text copied from a source as code.

```json
{
  "title": "A guided reading",
  "language": "en",
  "paper": {"id": "synthetic-example", "version": "v1"},
  "skill": {"version": "0.2.0-rc.1", "revision": "actual-local-revision"},
  "source_scope": "Synthetic illustration; no empirical claims.",
  "illustrated": true,
  "sections": [{
    "heading": "What changes in the mechanism",
    "html": "<p>Define each symbol beside its first use.</p><math xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow></math>",
    "figures": [{
      "path": "mechanism.png",
      "alt": "Description of the mechanism visible in the crop",
      "caption": "Mechanism used in this teaching example",
      "source": "Synthetic source, Figure 1",
      "page": 1,
      "kind": "teaching",
      "explanation_html": "<p>Explain what to inspect and what the figure does or does not establish.</p>"
    }]
  }]
}
```

`paper.url` is optional and must be an http(s) source link. `page` is the positive **1-based PDF page**, not a guessed printed page label. `kind` must be `original`, `reconstructed`, or `teaching`; label reconstruction and illustrative values clearly. An original crop retains the source's axes and legends. Every included image needs alt text, a caption, source locator, page and substantive adjacent explanation. Set `illustrated: false` only for an intentional text-only artifact; it is not a fallback that silently satisfies an illustrated request.

`html` and `explanation_html` accept a small set of semantic text/table/list tags, citation links and native MathML. Write Unicode symbols or numeric XML entities in MathML; HTML-only named entities may fail XML checks. Raw LaTeX is not rendered by this tool. Convert it carefully to MathML, use a verified equation image, or use the host's existing math renderer and equivalent artifact checks. Do not paste arbitrary HTML or active SVG from a fetched page. Unsupported tags/attributes fail with an error instead of being silently stripped.

## What the result means

`build` writes the file only after validation and refuses to overwrite the input manifest or images. `check` validates reports made with this template; it is not a general web-page validator. Nonzero exit status means failure. Checks cover required source/revision metadata, missing files, supported image signatures/base64, passive SVG structure, balanced supported HTML, valid MathML XML, unfinished placeholder markers, declared image counts, one image and caption per figure and absence of external rendering dependencies. Deleting an entire figure is detected against the declared count. It catches common raw-LaTeX remnants, not every possible notation error. PNG/JPEG checks validate signatures/end markers, **not full image decoding**; rendering remains mandatory.

The JSON result explicitly leaves visual inspection `not_run` and scientific accuracy/reuse permission `not_checked`. A script cannot establish readable labels, correct interpretation, valid numerical claims, permission to reuse a figure, or actual host delivery. Record those separately after observing them. Never rewrite these fields as passed merely because the command succeeded.
