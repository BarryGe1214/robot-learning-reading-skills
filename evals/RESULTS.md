# Evaluation status

Candidate: **0.2.0-rc.1**, local review on 2026-11-17, based on `a7a026befe8cf04a448633729299f50aa9e11d4d`. No remote push, release tag, installation or marketplace publication was performed. Acceptance is the existing local paper-reading workflow; cross-client and Agensi testing is outside this iteration.

| Check | Observed result | Meaning |
| --- | --- | --- |
| `node scripts/validate.mjs` | pass | Entry, links, versions, accompanying licenses and evaluation schema |
| `git diff --check` | pass | Patch formatting only |
| `python scripts/test-report-tools.py` | pass, 12 tests | Actual build/check CLI, missing and deleted figures, per-figure structure, external assets, source overwrite and markup failures |
| Standalone HTML rendering | pass | Current local browser, network requests blocked: one original figure loaded at 1475×720, one MathML block rendered, no external request or horizontal overflow; screenshot inspected for figure/caption and hat/subscript/superscript legibility |
| Prompt-isolated synthetic readings | 15 pass, 2 partial | 17 scenarios executed; criterion-level records and portable answer copies are below |
| Fresh ODE Policy reading | content spot-check pass; initial image-target failure corrected | Original PDF only, no old report; 2 original figures and equations. Not a full comparative benchmark |
| Generic skill-creator `quick_validate.py` | blocked | Existing Python lacks PyYAML; no dependency installed. Repository-specific validation above actually ran |
| Baseline/candidate comparison | not_run | No claim that the candidate outperforms the previous skill or no-skill baseline |
| Native final-chat rendering | not_run | Tool images, saved Markdown and browser HTML are distinct from observed delivery in the user's chat |
| Human reader acceptance | pending | Model grading does not replace the maintainer's judgment of explanation quality |

## Synthetic evidence

[Detailed judgments and hashes](runs/2026-11-17-rc1/results.json) contain a criterion-level result and exact output excerpt for every case. The saved answers are in the adjacent `outputs/` directory. Public copies preserve answer prose but replace machine-specific image links with the repository's synthetic SVG; hashes of the original local answers are retained. Raw traces and original targets remain in ignored `local/eval-outputs/`.

The two partial cases are `illustrated-default` and `illustrated-followup`: original-image inspection, explanatory content, image markup and actual target files were observed, but final-host rendering was not. They are **not** counted as full illustrated-delivery passes. The follow-up case supplies the previous preference in its prompt; it is not a test of memory across real sessions.

Fresh agents received only the skill, relevant references, prompt-only inputs and raw fixtures, without rubrics, expected answers or previous reports. Multiple cases shared each agent's context. The parent model graded the outputs; exact model version and sampling configuration are unknown. The first 16 cases ran before the final literal-image-path instruction; the added path case ran after it. Exact per-agent skill snapshots were not retained, so the recorded final package hashes must not be mistaken for the exact bytes each earlier agent read.

## Actual-paper regression and discovered failure

Source: *ODE Policy: Robot Learning via Action Dynamics, Not Actions*, arXiv:2611.01729v1 (2026-11-01), 35 pages. PDF SHA256: `b4654b6bbb5decfc7cac94d19ea721adfb2744ba5990a0e9b0888c34cfc65f5a`.

The fresh reading used a concrete placement example, separated commanded target from measured state, explained integration and perturbation supervision, and selected Figures 2 and 17. The parent checked the core mechanism and decisive ablation values against the source, including the different 79.2%/79.8% evaluation protocols and the no-offset result. This is a bounded spot-check, not certification of every claim. Original PDF/crops and the private reading are not included in public artifacts; local record: `local/ode-fresh/`.

The initial Markdown encoded the directory space as `%20`, making its filesystem image targets unsuitable for this host. The initial response is retained locally; copies were placed at authorized paths without spaces and the literal image references corrected. The instruction now requires verifying the final target itself. A fresh `literal-image-target` run inspected the supplied image and produced an existing, unencoded, space-free target. This is evidence of the targeted fix, not a retroactive pass for the initial report.

The HTML tool test also exposed an independent issue: checking equal image/caption totals alone could pass after an entire figure disappeared. The helper now stores the expected image count and checks one image/caption per figure. Both deletion and malformed-figure regressions were actually executed.

## Limits and release interpretation

This is a reviewable candidate validated against current local usage. Broader VLA/world-model/RL coverage, repeat runs, quantitative reading-quality estimates and comparative gains remain untested. Do not advertise platform compatibility or a fully empirically validated commercial product from these records. See the packaged ATTRIBUTION ledger for the bounded source review and accompanying notices; it does not claim exhaustive historical provenance clearance.
