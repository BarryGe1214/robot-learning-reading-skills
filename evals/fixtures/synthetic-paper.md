# Carrying a reference target: a synthetic paper

Synthetic evaluation material authored for this repository; MIT licensed. This is not a published paper or evidence about a real robot.

## 1. Problem
A tabletop arm follows reference targets. The baseline predicts a target chunk from the latest image and measured joint state. The candidate also receives the previous commanded target and predicts local target increments, accumulating them into a short chunk. This design aims to use the previous command as a starting point. The baseline is not asserted to be discontinuous.

## 2. Training and execution
The candidate is trained on demonstration reference targets with squared error on the accumulated targets. The loss supervises command targets, not measured states. Both methods use the same 50 demonstrations and low-level controller. The input observation is refreshed at the start of each chunk. A chunk has four targets sampled at 20 Hz, and two targets are executed before replanning; unexecuted targets are replaced. Controller commands are interpolated to 100 Hz. Inference latency, interpolation algorithm, disturbances and stability guarantees are not reported.

Figure 1 (synthetic original, `synthetic-figure.svg`) shows the command construction. The measured state conditions the update network; the accumulated target is a commanded reference. The dashed boundary denotes fixed observation during one chunk. The illustration is a mechanism diagram, not a measured trajectory.

## 3. Evidence
Table 1: after one training epoch the baseline completes 6 of 10 held-out trials and the candidate completes 8 of 10. Completion means the object reaches the marked region. A candidate variant initialized from measured state instead of the previous target completes 7 of 10. These are raw counts from one evaluation, without seed variation or confidence intervals. The table establishes an observed ordering under the stated conditions; it does not isolate the reason for the improvement. There is no stability theorem or closed-loop perturbation test.

## 4. Limits
The study tests one task. It does not establish performance on other embodiments or under contact, nor that smoothly changing reference commands imply stable measured motion.
