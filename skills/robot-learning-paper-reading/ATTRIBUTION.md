# Attribution and source ledger

Original additions to this package are distributed under the accompanying [MIT license](LICENSE), copyright 2026 BarryGe1214. Attributed upstream material retains its applicable license; do not describe the entire package as exclusively MIT or relicense the portions identified below as original text. Neither license covers papers, figures or other material supplied while using the skill.

## Design references

Checked on 2026-11-17 against the following fixed upstream revisions. These are **audit snapshots**, not a claim that the original development used those exact revisions. The originally consulted commits and file-level adaptation history are unknown. Earlier development records described conceptual reference without recording source-file imports. The bounded review below identified close structural correspondences, so those portions are conservatively tracked as suspected adaptations with upstream notices included. A complete historical text-adaptation audit has not been performed.

| Source and audit revision | Relevant source file inspected | Recorded design influence | License verified at that revision |
| --- | --- | --- | --- |
| [techdou/paper-reading](https://github.com/techdou/paper-reading/tree/1271fbfbe84c6e69506f2c56c94599f0d6d427da), `1271fbfbe84c6e69506f2c56c94599f0d6d427da` | [SKILL.md](https://github.com/techdou/paper-reading/blob/1271fbfbe84c6e69506f2c56c94599f0d6d427da/SKILL.md) | Reading depth, mechanism reconstruction, evidence checks | [Apache-2.0](https://github.com/techdou/paper-reading/blob/1271fbfbe84c6e69506f2c56c94599f0d6d427da/LICENSE); [NOTICE.md](https://github.com/techdou/paper-reading/blob/1271fbfbe84c6e69506f2c56c94599f0d6d427da/NOTICE.md) credits 成峰 / AI产品自由 and the original [Agentchengfeng/paper-reading-skills](https://github.com/Agentchengfeng/paper-reading-skills) |
| [JinPLu/clear-eyed-reading-skills](https://github.com/JinPLu/clear-eyed-reading-skills/tree/75ce1c5c9eaa159dd8142237085cae72fbea9afc), `75ce1c5c9eaa159dd8142237085cae72fbea9afc` | [skills/clear-eyed-deep-reading/SKILL.md](https://github.com/JinPLu/clear-eyed-reading-skills/blob/75ce1c5c9eaa159dd8142237085cae72fbea9afc/skills/clear-eyed-deep-reading/SKILL.md) | Running examples, contribution attribution | [MIT](https://github.com/JinPLu/clear-eyed-reading-skills/blob/75ce1c5c9eaa159dd8142237085cae72fbea9afc/LICENSE), copyright 2026 JinPLu |
| [UCL-ERL/skills](https://github.com/UCL-ERL/skills/tree/9d50603850b661a1da175ef3e330ba0b52e3efe9), `9d50603850b661a1da175ef3e330ba0b52e3efe9` | [skills/research/paper-reading-card/SKILL.md](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/research/paper-reading-card/SKILL.md) | Robotics evidence and reusable reading cards | [MIT](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/LICENSE), copyright 2026 ERL Lab contributors |
| [licongxu/cosmo-agent-skills](https://github.com/licongxu/cosmo-agent-skills/tree/6174ecc6accf59abb9ab5d4e8d06824667a753fb), `6174ecc6accf59abb9ab5d4e8d06824667a753fb` | [skills/paper-reading/paper-deep-reading/SKILL.md](https://github.com/licongxu/cosmo-agent-skills/blob/6174ecc6accf59abb9ab5d4e8d06824667a753fb/skills/paper-reading/paper-deep-reading/SKILL.md) | Three-pass reading and traceable notes | [MIT](https://github.com/licongxu/cosmo-agent-skills/blob/6174ecc6accf59abb9ab5d4e8d06824667a753fb/LICENSE), copyright 2026 Licong Xu |

## Bounded review 2026-11-17

Reviewed the current SKILL.md and all eight reading reference files against the four source entries linked above, plus techdou's `references/reading-workflow.md`, `references/output-contracts.md`, `references/evidence-quality.md`, and cosmo's `skills/paper-reading/paper-deep-reading/references/note-schema.md`, at the same pinned commits. Read the source texts directly and compared the reading logic and expression; a supplementary case-insensitive English token scan found no identical contiguous sequence of seven or more words. That scan does not detect translation or paraphrase and is not a legal threshold or proof of originality. Scripts, templates, other upstream files and earlier history were outside this review.

The following current passages closely follow techdou's ordered reading patterns. Treat them as **suspected structural/text adaptation** for distribution, without claiming that this comparison reconstructs their historical origin:

| Current portion in SKILL.md | Corresponding upstream portion | Current rewrite |
| --- | --- | --- |
| Pass 1, causal chain | techdou SKILL.md, Operating objective; reading-workflow.md §4.2 | Compresses problem and prior limitation into a bottleneck, adds decision process and expected capability, and retains the design-action/information-flow/evidence sequence |
| Pass 2, module explanation | techdou SKILL.md, Core workflow §4; reading-workflow.md §9.2 | Rephrases the ordered purpose/input/operation/output/connection/benefit sequence; handles experimental support in the separate evidence pass |
| Pass 2, equation explanation | techdou SKILL.md, Core workflow §4; reading-workflow.md §9.3 | Rephrases the question/symbols/operation/intuition/implementation sequence and adds dimensions, assumptions and a no-invented-derivations constraint |

The applicable [Apache-2.0 license](third-party/techdou-paper-reading/LICENSE) and [upstream NOTICE](third-party/techdou-paper-reading/NOTICE.md) accompany the package unchanged from the pinned audit snapshot. They retain attribution to 成峰 / AI产品自由 and Agentchengfeng/paper-reading-skills as well as identifying the inspected techdou fork. This section and the source note in SKILL.md record the modifications. Preserve them and the third-party directory when redistributing these portions.

The other inspected sources share reading ideas such as a running example, evidence-sensitive interpretation and three-pass reading. This bounded check did not establish a specific copied passage from them; the absence of an identified match does not establish originality or clear unexamined adaptations. Keep their design credits and update this record if concrete reuse is identified.

## When incorporating upstream expression or code

Record the exact upstream commit and file, the destination file/portion, whether it is copied, translated or adapted, and the modifications. Do not classify textual adaptation as conceptual inspiration simply because wording changed.

- For MIT material, retain the upstream copyright and permission notice with copies or substantial portions; our own LICENSE is not a substitute.
- For Apache-2.0 material, provide its license, retain applicable source notices and NOTICE attribution, and mark modified files. The linked techdou NOTICE includes attribution to the original author, not only the fork owner. Links in this ledger alone do not satisfy a required accompanying license or notice.
- Check file-specific exceptions and third-party assets separately. Do not imply upstream endorsement or change third-party licensing to this package's MIT license.

Both listed license types permit commercial distribution subject to their conditions. This ledger records the inspected evidence and remaining provenance gaps; it is not a declaration that unexamined material has been cleared. Preserve LICENSE and this ledger when distributing the skill directory.
