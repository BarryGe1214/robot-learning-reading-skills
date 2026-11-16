# Robot-learning checks

Apply only relevant checks. Missing information is unreported, not inferred.

## VLA and imitation learning
Identify modalities, proprioception, language conditioning and their roles. Define action semantics (joint/Cartesian, position/velocity/force/latent), absolute vs delta, coordinates, units and normalization. Distinguish latent-action prediction from executable robot commands. Check action decoder, chunk length, temporal stride, training targets and execution schedule. Check data mixture, supervision, pretrained capability and held-out splits before attributing gains.

## World models and WAM
Use the paper's own expansion of WAM. Determine predicted variables, action conditioning and temporal horizon. Identify whether the model supports representation learning, synthetic training data, planning, value estimation or direct action generation.
Separate appearance quality, prediction fidelity, action controllability, physical executability and closed-loop task outcomes. Ask whether rollout errors compound and whether the planner can exploit model errors. Video prediction alone does not demonstrate causal dynamics or manipulation competence.

## RL and learned control
Identify observations, actions, rewards, privileged training information, deployment sensors, policy rate and lower-level controllers. Examine randomization, simulator assumptions, contacts and sim-to-real evaluation. State which performance comes from the policy, reward engineering, reset distribution, controller or task constraints.

## Teleoperation and cross-embodiment
Determine correspondence between human motion, reference targets, command trajectories and measured robot execution. Check kinematic/dynamic feasibility, retargeting, embodiment conditioning, calibration and action-label provenance. Do not equate a human pose or commanded pose with an achieved robot state.

## Hybrid systems and timing
Locate IK, trajectory planners, impedance control, MPC/WBC, safety layers and human corrections. Distinguish model generation rate, action sampling rate, command update rate, low-level servo rate and replan rate.
Inspect observation timestamps, latency, chunk execution horizon, overlap, interpolation and smoothing when deployment claims depend on them. A generated trajectory is not measured motion.

## Experiments and generalization
Record trial counts, distributions, resets, intervention rules, success definitions and uncertainty where available. Distinguish offline metrics, simulation and real robots.
Specify whether generalization concerns objects, scenes, tasks, language, embodiments or dynamics. Check overlap and selection effects. Do not compare raw success rates across incompatible settings. Separate added data/compute or stronger controllers from algorithmic contributions.

## Theory, datasets and surveys
For theory inspect assumptions, applicability and proof steps that carry the result. For datasets inspect provenance, consent where relevant, coverage, annotation and train/test leakage. For surveys inspect selection scope and contradictory evidence. Do not require every work to contain real-robot trials.
