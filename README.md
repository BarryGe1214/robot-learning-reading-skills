# Robot Learning Reading Skills

面向机器人学习研究者的证据驱动论文精读 skill，覆盖 VLA、世界模型与动作模型、模仿学习、RL、遥操作、跨本体迁移，以及学习策略与控制系统的结合。

**当前候选版本：0.2.0-rc.1（本地审阅，未发布）。** 以已有中文机器人学习精读场景验收：机制导读、原图解释、公式和证据核对、聚焦追问。结构检查、模型行为与实际文件目视检查分别记录，详见 [评测记录](evals/RESULTS.md)。跨客户端和 Agensi 实测不属于本轮验收，也不作兼容性承诺。

## 使用
可分发入口为 [SKILL.md](skills/robot-learning-paper-reading/SKILL.md)。将整个 `skills/robot-learning-paper-reading/` 目录交给客户端安装流程，保留 references、scripts、third-party、LICENSE、ATTRIBUTION.md 和 VERSION。客户端的加载路径及调用语法以其当前文档为准；GitHub 存储不等于 ChatGPT 已安装。当前修改不安装到任何客户端，也不自动发布。

不支持安装 skill 时，在新对话中提供入口及所需 reference 文件，并要求按它们阅读论文。仅分享仓库链接不保证助手已经读取文件。项目指令可引用这套规则，但避免维护第二份完整副本。

示例：
- “使用 robot-learning-paper-reading 分析这篇论文，先给机制、证据和阅读路线。”
- “用同一个例子走通训练与推理，详细解释核心公式。”
- “检查实验是否支持核心主张，区分系统收益、组件收益和机制解释。”

使用用户要求的语言，否则跟随当前请求；无法判断时使用中文。先结论、分层深入。要求精读时完整分析，但不强制将所有检查项写进回答。来源不全时明确缩小结论范围。

## 运行要求与交付
整篇精读需要准确版本的正文、相关附录及图表访问；图文文件还需要图片查看、文件生成与最终渲染能力。没有相关能力时只交付已验证范围，并说明具体缺口。短问题不强制生成文件。私有论文默认沿用户授权的读取路径处理，普通阅读不要求重复审批。

可选 [报告工具](skills/robot-learning-paper-reading/references/report-tools.md) 用 Python 3.10+ 标准库把已写好的解释、公式和已检查原图生成自包含 HTML；它不代替论文理解。PDF 解析和裁图使用宿主现有工具。无需为阅读自动安装依赖或接入新服务。

## 仓库结构
- `skills/`：唯一可分发 skill 源码；公共 reader-profile 不含维护者个人信息。
- [GOVERNANCE.md](GOVERNANCE.md)：范围、决策权、证据、隐私及版本规则。
- [AGENTS.md](AGENTS.md)：自动化代理修改仓库时必须遵守的约束。
- [CONTRIBUTING.md](CONTRIBUTING.md)：反馈、提交、评测和发布流程。
- [CHANGELOG.md](CHANGELOG.md)、[VERSION](VERSION)：可追溯版本。
- [evals/](evals/README.md)：合成回归用例和结果记录。
- `scripts/validate.mjs`：零第三方依赖的结构校验；Node.js 20+。

## 更新与验证
运行 `node scripts/validate.mjs`。报告工具检查用 `python scripts/test-report-tools.py`；隔离评测输入用 `node scripts/prepare-eval.mjs`。每个行为变更需记录具体失败、最小修订和相应用例；模型试读和实际渲染分别记录，不能以静态检查代替。

提交记录保存每次修改，版本标签标记可复用快照。安装后的副本不会自动随仓库更新；升级时记录所用标签或 commit，完整替换 skill 目录并确认客户端加载版本。

本仓库自有新增内容采用 MIT License；已标注的 techdou 可能改编部分保留 Apache-2.0 及随包 NOTICE。设计参考、固定核验版本与有界比对记录见 [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md)。上述许可不覆盖被阅读论文及其原图；当前原图报告仅用于授权阅读验证，不作为付费附赠或公开营销素材。本仓库不包含受限论文全文、私人阅读笔记或公司内部资料。
