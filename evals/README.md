# Evaluation

cases.json contains synthetic prompts and independent rubrics. Feed only prompt plus the skill and required references to the evaluated assistant; never feed rubric. Record raw output, source scope, model/version (unknown if unavailable), date, exact skill commit and judgments. Public outputs must contain no private data.

Run `node scripts/prepare-eval.mjs` to write prompt-only JSONs under ignored `local/eval-inputs/`. Pass only the chosen JSON and its `input_files` to a fresh context; do not expose cases.json, prior reports, patch rationale or expected answers. Illustrated cases include an original MIT-licensed synthetic paper and SVG fixture, rather than claiming an unavailable attachment exists. Raw synthetic answers may be retained in the evaluation record; real-paper PDFs/crops and private reports stay outside public version control.

Judge each criterion pass/fail/uncertain with an output excerpt; do not average away fabricated facts. Any fabricated evidence or false full-reading claim blocks a behavioral release. Structural CI is independent and cannot produce behavioral passes.

Real-paper coverage should eventually include one VLA, one world/action model and one RL/control paper with exact public version identifiers. This is planned coverage, not a claim of completed tests. Do not commit copyrighted full papers.

The 0.2.0-rc.1 acceptance scope is the current local reading workflow: source access, causal explanation, figures/formulas, evidence limits and concise follow-ups. Cross-client and Agensi testing is deferred by scope, not a failed acceptance gate. A fresh ODE Policy reading is a single-paper regression check, not a three-domain benchmark or proof of superiority to the baseline.

For comparative changes keep model, prompt and input fixed when feasible. Save both baseline and candidate outputs. A single run is a regression signal, not an accuracy estimate.
