# Changelog

## Unreleased

## 0.2.0-rc.1 — 2026-11-17
Local review candidate; no release tag, remote push, client installation or marketplace publication.
- Scope acceptance to the existing local paper-reading workflow; defer cross-client and Agensi tests.
- Add capability-aware delivery, language/context reuse and separate private reading from public sample reuse.
- Add a standalone illustrated HTML helper, image/source checks and executable failure-case tests; mechanical results do not certify rendering or scientific accuracy.
- Include VERSION, LICENSE and a fixed-snapshot attribution ledger inside the distributable skill directory; retain unknown historical provenance explicitly.
- Supply real synthetic fixture inputs and prompt-only evaluation exports; record raw model outputs separately from rubrics.
- Correct a fresh ODE reading's encoded local-image path failure; require literal verified image targets and a safe local copy when the host needs one.
- Add a causal guided-reading narrative: a running example and mapped analogy precede equations, with experiments testing the proposed intuition and secondary audit details kept out of the main thread.
- Default whole-paper readings to illustrated delivery, preserve the requirement across follow-ups, and separate code exclusion from figure coverage.
- Require final-report render checks and original-image explanation in the final response; captions, tool images and link-only responses do not pass the delivery gate.
- Add explicit uploaded-PDF figure extraction and visual verification workflow; record access-stage failures and local-only review scope.
- Add original-figure-access case and manual evaluation record; current verification status is recorded in evals/RESULTS.md.
- 初读改为可独立理解的证据导读：关键原文、公式或验证过的数据紧邻解释；保留出处与实验条件。
- 区分原文、译述、推断、原图与重排表格；图像不可访问时明确降级，不编造数值。
- 增加 self-contained-evidence 合成用例；本地审阅中，未发布。

## 0.1.0 — 2026-11-16
- 建立机器人学习论文精读入口，以及领域检查、阅读模式和通用读者配置。
- 加入主张—证据区分、训练/部署接口、动作时序和世界模型闭环收益核查。
- 建立治理、贡献、代理约束、回归用例和静态校验流程。
- 评测状态：结构校验可执行；真实论文阅读效果尚未验证，不声明准确率或收益。
