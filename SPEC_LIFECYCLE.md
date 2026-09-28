# Spec Lifecycle

```text
Idea
→ Intake
→ Grill (P0/P1/P2)
→ GCCSEG Check
→ Converge
→ Spec
→ Architecture
→ PROJECT_ROADMAP
→ Spike? (only if necessary)
→ Current Phase
→ Plan
→ Tasks / Work Packages
→ SCP Preflight
→ Implement
→ Evidence
→ Phase Gate
→ Advance Phase (if PROJECT_COMPLETE=false)
→ Project Completion Gate (only when PROJECT_COMPLETE=true)
→ Handoff / Freeze
```

## Phase 与 Project 的区别

- **Phase PASS ≠ Project Complete**。
- `PROJECT_ROADMAP.md` 是总工程进度牌：定义阶段、当前 Phase、下一步与项目完成条件。
- 每个 Phase 可以有自己的 Parent Work / Child WPs / Acceptance / Evidence。
- 当前 Phase PASS 后，如果 `PROJECT_COMPLETE=false`，必须继续下一 Phase；阶段汇报不是停机点。
- 只有 `PROJECT_COMPLETE=true` 且 Project Completion Gate 有独立 Evidence，才能整体封箱。
- Roadmap 是导航，不得成为第二运行时状态源。

## Spike 的定义

Spike 只用于验证一个会改变技术方案的未知，例如：
- 某同步工具是否支持既有大文件只传差异
- 某第三方 API 是否能返回必须的字段
- 某模型在固定样本上的质量是否达标

Spike 必须：
- 单问题
- 时间盒化
- 有明确结论格式
- 不演变成正式产品代码
