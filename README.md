# Robot Learning Reading Skills

面向机器人学习研究者的证据驱动论文精读 skill，覆盖 VLA、世界模型与动作模型、模仿学习、RL、遥操作、跨本体迁移，以及学习策略与控制系统的结合。

**当前版本：0.1.0。** 初版为指令规范；通过结构检查不代表已证明阅读效果。实际论文对测状态见 [评测记录](evals/RESULTS.md)。

## 使用
可分发入口为 [SKILL.md](skills/robot-learning-paper-reading/SKILL.md)。将整个 `skills/robot-learning-paper-reading/` 目录交给支持 Agent Skills 的客户端安装流程，不要只复制入口而漏掉 references。客户端的加载路径及调用语法以其当前文档为准；GitHub 存储不等于 ChatGPT 已安装。

不支持安装 skill 时，在新对话中提供入口及所需 reference 文件，并要求按它们阅读论文。仅分享仓库链接不保证助手已经读取文件。项目指令可引用这套规则，但避免维护第二份完整副本。

示例：
- “使用 robot-learning-paper-reading 分析这篇论文，先给机制、证据和阅读路线。”
- “用同一个例子走通训练与推理，详细解释核心公式。”
- “检查实验是否支持核心主张，区分系统收益、组件收益和机制解释。”

默认中文、先结论、分层深入。要求精读时完整分析，但不强制将所有检查项写进回答。来源不全时明确缩小结论范围。

## 仓库结构
- `skills/`：唯一可分发 skill 源码；公共 reader-profile 不含维护者个人信息。
- [GOVERNANCE.md](GOVERNANCE.md)：范围、决策权、证据、隐私及版本规则。
- [AGENTS.md](AGENTS.md)：自动化代理修改仓库时必须遵守的约束。
- [CONTRIBUTING.md](CONTRIBUTING.md)：反馈、提交、评测和发布流程。
- [CHANGELOG.md](CHANGELOG.md)、[VERSION](VERSION)：可追溯版本。
- [evals/](evals/README.md)：合成回归用例和结果记录。
- `scripts/validate.mjs`：零第三方依赖的结构校验；Node.js 20+。

## 更新与验证
运行 `node scripts/validate.mjs`。每个行为变更需记录具体失败、最小修订和相应用例；人工/模型试读结果单独记录，不能以静态检查代替。

提交记录保存每次修改，版本标签标记可复用快照。安装后的副本不会自动随仓库更新；升级时记录所用标签或 commit，完整替换 skill 目录并确认客户端加载版本。

本仓库采用 MIT License。阅读流程设计的参考来源见 [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md)。不包含论文全文、私人阅读笔记或任何公司内部资料。
