# Illustrated delivery regression

Date: 2026-11-16
Base: cb03da6 plus the delivery-contract changes in this commit.
Runtime model identifier: unknown.

## Observed failure and change

A whole-paper reading returned only prose after an earlier illustrated-report request. Figure inspection instructions alone did not preserve the output requirement. The previous access-failure case checked honesty when images were unavailable, but never exercised successful acquisition through final delivery.

Whole-paper readings now default to relevant original illustrations. Code exclusion does not disable images. Final-report rendering and final-response image embedding are distinct checks. Focused questions and explicit text-only requests remain exempt.

## Independent forward check

A fresh agent received the changed skill, the public ODE Policy PDF (arXiv:2611.01729v1), extracted source text, and original figure files. No diagnosis, expected response, rubric, previous report or patch rationale was supplied. It was asked for an initial paper reading, skipping code and not creating a downloadable file.

Raw task prompt (translated only for this record): “Analyze this paper, skip code analysis, focus on the paper itself, and give an initial guided reading.”

Observed response excerpts:

> 图 2 左侧一次预测整段动作；右侧从上一个动作出发，逐步生成后续动作，跨 chunk 也延续同一个动作状态。底部曲线是机制示意，不是实测轨迹。

> 此处每任务评估 10 次，因此与主结果的 79.2% 不同。

The returned response actually included two Markdown image embeds: the supplied original Figure 2 and Figure 17 crops, each immediately followed by explanation. It defined the action/state distinction, separated streaming execution from observation refresh, and retained the random-initialization qualification for the VLA comparator.

Assessment: pass for default illustration selection and final-response embedding; pass for attached explanations and source/evidence boundaries. This is an independent output check, not a client-rendering test or a full scientific-accuracy benchmark. The source checkout HEAD remained cb03da6 during this check; the agent read the modified working-tree skill, not the old committed body.

## Manual counterchecks

- Explicit text-only or focused equation question: instruction inspection confirms no mandatory full illustrated report. Independent response run: not_run.
- Tool-output image or a caption without report embedding: fails the new completion contract. Automated runtime gate: not implemented.
- Missing image bytes: must disclose the incomplete stage; must not fabricate a crop. New independent blocked-transfer run: not_run; previous figure-access review remains limited to its recorded case.

Structural validation: node scripts/validate.mjs passed. Remaining general behavioral suite: not_run. No public repository contains the paper PDF, original figure files, private paths or full user conversation.
