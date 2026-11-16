# Evaluation

cases.json contains synthetic prompts and independent rubrics. Feed only prompt plus the skill and required references to the evaluated assistant; never feed rubric. Record raw output, source scope, model/version (unknown if unavailable), date, exact skill commit and judgments. Public outputs must contain no private data.

Judge each criterion pass/fail/uncertain with an output excerpt; do not average away fabricated facts. Any fabricated evidence or false full-reading claim blocks a behavioral release. Structural CI is independent and cannot produce behavioral passes.

Real-paper coverage should eventually include one VLA, one world/action model and one RL/control paper with exact public version identifiers. This is planned coverage, not a claim of completed tests. Do not commit copyrighted full papers.

For comparative changes keep model, prompt and input fixed when feasible. Save both baseline and candidate outputs. A single run is a regression signal, not an accuracy estimate.
