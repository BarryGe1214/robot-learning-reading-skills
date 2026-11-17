# Guided-reading narrative

Use for initial interpretations and full paper guides. A guide should let the reader reconstruct why the method exists, not merely inventory modules and verify claims. Preserve the source and illustration requirements in SKILL.md.

## Build the explanation

1. Open with one concrete situation in which the prior approach faces the paper's bottleneck. Identify what the policy knows, predicts and executes. Label an invented example as teaching material.
2. Explain the central change in everyday, operational language. Give the reader a compact mental model before symbols or module names. Avoid caricaturing baselines: say when an issue is possible rather than inevitable.
3. Follow the same example through the change. Each subsequent module should answer a question the example has just raised: how is this learned, what happens after an error, or how are alternative outcomes represented?
4. Introduce each essential equation only after naming the question it answers. Map the example to the symbols and explain the operation in words. Keep the exact technical account close enough that the analogy cannot replace it.
5. Use experiments to test the resulting expectations, rather than enumerate benchmarks in paper order. Explain what outcome would support or contradict the intuition before presenting a decisive figure.
6. End with the supported mental model and a short route back to the source. Keep extensive configuration, statistical caveats and implementation detail in secondary paragraphs or expandable notes when they are not needed for first understanding. Retain nearby qualifications that change the meaning of the main claim.

## Use analogies precisely

- Prefer one coherent analogy or running task over many unrelated metaphors. Do not require an analogy where direct explanation is clearer.
- State the correspondence: which part represents the observation, learned operation, intermediate variable and output? Distinguish command from measured state, computation from execution, and prediction from control.
- State one important limit immediately when the analogy could mislead. A continuous curve is not automatically a stable controller; a planning analogy does not imply an actual search algorithm.
- Use illustrative numbers only when labeled synthetic, and never present the example as experimental evidence.
- Avoid fictional author intentions, anthropomorphism, or familiar metaphors with no operational correspondence.

## Check flow before delivery

The first few paragraphs should answer: what problem appears, what changes, and why that change could help. Each section should create or answer a question leading to the next. The same example should survive the transition from intuition to the equation and from training to deployment. Check that a technically informed reader can explain the central mechanism without opening a table or following a source link.

Scientific criticism remains necessary, but organize it around the claims already understood. Do not open every paragraph by denying an exaggerated claim the reader has not made. Focused questions and evidence-audit requests may use a different order.
