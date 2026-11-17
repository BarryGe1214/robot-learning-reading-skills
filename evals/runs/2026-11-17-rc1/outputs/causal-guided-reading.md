**The central change is to predict how to continue from the previous reference target, rather than predict an entire future target sequence afresh.** Think of a robot approaching a placement location: the old policy outputs the next short path together; the proposed policy carries its last target forward and builds a new path by repeatedly applying a learned local update. This placement example is illustrative, not an experiment reported in the supplied material.

What does the carried target contribute? It gives construction of the new command path an explicit starting point. Each update changes that target, and the resulting targets form the short path. The relevant memory is a **commanded reference**, not proof of where the robot currently is. The baseline need not be discontinuous, and accumulated updates can still be large; this design alone does not establish smoothness.

To express that operation, let \(r_0\) be the retained target, \(r_j\) the constructed target after update \(j\), and \(\Delta r_j\) the learned increment. A schematic additive representation is

\[
r_{j+1}=r_j+\Delta r_j.
\]

This equation explains the accumulation; it is not a quoted paper equation. The supplied account does not specify the update network's full inputs, parameterization or loss. It does specify that training supervises the **resulting short path**: the learning signal therefore evaluates what the sequence of updates produces, rather than establishing that any particular local update is a correct dynamics model.

During deployment, the observation is refreshed once per chunk. Thus the repeated updates within a chunk can use the same observation; they are not repeated measurements of the robot responding to commands. The text does not specify how much of a chunk is executed before replanning. A target carried forward can differ from the achieved state after tracking error, so this mechanism should not be interpreted as continuous feedback correction.

The reported faster early learning is consistent with the proposed construction making the supervised problem easier. It does not identify that as the cause: no comparator details or quantitative results are provided here. Nor does it establish stability—there is no proof, and early learning speed is a different property from bounded closed-loop behavior. The useful reading question is therefore whether carrying the last target and composing local updates improves learning under matched conditions; stability would require separate assumptions and evidence. This reading covers only the supplied synthetic description, which contains no accessible figure or numerical table.
