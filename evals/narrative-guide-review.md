# Guided narrative evaluation

Date: 2026-11-16. Base: 5ecbe27 plus this working-tree change.
Runtime model identifier: unknown.

## Failure and change

The illustrated ODE Policy reading preserved evidence but interrupted understanding with module inventories and repeated caveats. Add a progressively loaded narrative reference: concrete situation, operational intuition, causal questions, equations, then experiments. Require explicit analogy mappings and limits without weakening source standards.

## Independent forward check

A fresh evaluation agent received the modified skill and public ODE Policy source extracts (arXiv:2611.01729v1, pages 2, 6, 7, 8), plus Figure 2. It did not receive the existing report, diagnosis, expected answer or rubric. Task: write an approximately 600-character guided opening explaining what the paper changes; no complete report requested.

Observed output opened with a labeled cup-reaching teaching example, explained generation as continuation from the previous command, then introduced the question of accumulated error and the role of perturbed-start training. It explicitly distinguished command from measured position and execution time from denoising time. It explained trajectory supervision without velocity labels and did not claim stability from continuity.

Assessment: pass for causal progression, concrete example and technical mappings. The output used a running task rather than an elaborate metaphor, which is permitted. One sentence about reading measured state could still be interpreted as per-step feedback if isolated; the full rewritten report explicitly states observation/state freezing within a chunk. This focused check does not establish whole-report behavior or universal improvement.

## Report and structural checks

The full ODE Policy report was separately rewritten around a single reference-pen analogy. Training, perturbations and multimodal choices answer questions raised by the same example. Experiments follow those expectations; essential comparator qualifications remain adjacent, while secondary details are expandable.

Artifact checks: ten embedded image assets decode, seven MathML blocks parse, no external image dependencies. Browser preview showed the rewritten opening and original Figure 2; all ten images reported complete with natural width 1475 pixels. Remaining original figures were unchanged from their previous visual inspection.

Structural validation: `node scripts/validate.mjs` passed.
New synthetic case `causal-guided-reading`: added; independent execution not_run (the public-paper forward check above is separate).
Unrelated modes and full behavioral suite: not_run. No installation, remote push or release performed. Paper bytes, report and private local paths are excluded from this repository.
