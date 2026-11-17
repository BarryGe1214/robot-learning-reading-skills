"""Artifact regression checks using only synthetic source data and stdlib."""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("report_tool", ROOT / "skills/robot-learning-paper-reading/scripts/report_tool.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="reading-report-test-")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "figure.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="30"><text x="5" y="20">Synthetic</text></svg>', encoding="utf-8")
        self.manifest = {
            "title": "Synthetic guide", "paper": {"id": "synthetic-test", "version": "v1"},
            "skill": {"version": "test", "revision": "test-revision"},
            "source_scope": "Synthetic source; no paper claims.",
            "sections": [{"heading": "Mechanism", "html": '<p>A synthetic relation.</p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>',
                          "figures": [{"path": "figure.svg", "alt": "Synthetic text figure", "caption": "Synthetic figure", "source": "Synthetic source, Figure 1", "page": 1, "kind": "teaching", "explanation_html": "<p>This is a test asset, not experimental evidence.</p>"}]}]}

    def build(self):
        manifest_path = self.root / "manifest.json"
        manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")
        return tool.build(manifest_path, self.root / "report.html")

    def test_standalone_roundtrip(self):
        result = self.build()
        self.assertEqual(result["embedded_images"], 1)
        self.assertEqual(result["mathml_blocks"], 1)
        self.assertEqual(result["visual_inspection"], "not_run")
        text = (self.root / "report.html").read_text(encoding="utf-8")
        self.assertEqual(tool.check_html(text)["status"], "pass")
        self.assertNotIn(str(self.root), text)

    def test_missing_image_fails_without_output(self):
        self.manifest["sections"][0]["figures"][0]["path"] = "absent.png"
        with self.assertRaisesRegex(tool.ReportError, "Missing image"):
            self.build()
        self.assertFalse((self.root / "report.html").exists())

    def test_missing_images_not_silently_text_only(self):
        self.manifest["sections"][0]["figures"] = []
        with self.assertRaisesRegex(tool.ReportError, "no images"):
            self.build()

    def test_external_asset_rejected(self):
        self.manifest["sections"][0]["html"] = '<img src="https://example.org/figure.png" alt="external">'
        with self.assertRaises(tool.ReportError):
            self.build()

    def test_active_svg_rejected(self):
        (self.root / "figure.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>', encoding="utf-8")
        with self.assertRaisesRegex(tool.ReportError, "active"):
            self.build()

    def test_raw_latex_rejected(self):
        self.manifest["sections"][0]["html"] = r"<p>\(x\)</p>"
        with self.assertRaisesRegex(tool.ReportError, "Unrendered LaTeX"):
            self.build()

    def test_metadata_and_placeholder_rejected(self):
        self.manifest["skill"]["revision"] = "TODO"
        with self.assertRaisesRegex(tool.ReportError, "placeholder"):
            self.build()

    def test_corrupted_embedded_image_rejected(self):
        self.build()
        text = (self.root / "report.html").read_text(encoding="utf-8")
        text = text.replace("data:image/svg+xml;base64,", "file:///missing.svg?payload=")
        with self.assertRaisesRegex(tool.ReportError, "embedded"):
            tool.check_html(text)

    def test_deleted_figure_rejected(self):
        self.build()
        text = (self.root / "report.html").read_text(encoding="utf-8")
        text = re.sub(r"<figure>.*?</figure>", "", text, flags=re.S)
        with self.assertRaisesRegex(tool.ReportError, "delivery contract"):
            tool.check_html(text)

    def test_two_images_in_one_figure_rejected(self):
        self.build()
        text = (self.root / "report.html").read_text(encoding="utf-8")
        image = re.search(r"<img\b[^>]*>", text)[0]
        text = text.replace(image, image + image)
        with self.assertRaisesRegex(tool.ReportError, "exactly one image"):
            tool.check_html(text)

    def test_input_image_cannot_be_overwritten(self):
        self.build()
        original = (self.root / "figure.svg").read_bytes()
        with self.assertRaisesRegex(tool.ReportError, "overwrite"):
            tool.build(self.root / "manifest.json", self.root / "figure.svg")
        self.assertEqual((self.root / "figure.svg").read_bytes(), original)

    def test_cli_build_check_and_failure(self):
        self.build()
        script = str(ROOT / "skills/robot-learning-paper-reading/scripts/report_tool.py")
        run = subprocess.run([sys.executable, script, "build", str(self.root / "manifest.json"), str(self.root / "cli.html")], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout)["embedded_images"], 1)
        run = subprocess.run([sys.executable, script, "check", str(self.root / "cli.html")], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        (self.root / "figure.svg").unlink()
        run = subprocess.run([sys.executable, script, "build", str(self.root / "manifest.json"), str(self.root / "failure.html")], capture_output=True, text=True)
        self.assertEqual(run.returncode, 1)
        self.assertEqual(json.loads(run.stderr)["status"], "fail")
        self.assertFalse((self.root / "failure.html").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
