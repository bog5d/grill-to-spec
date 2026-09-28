# Spec Lifecycle

```text
Idea
→ Intake
→ Grill (P0/P1/P2)
→ GCCSEG Check
→ Converge
→ Spec
→ Architecture
→ Spike? (only if necessary)
→ Plan
→ Tasks / Work Packages
→ SCP Preflight
→ Implement
→ Evidence
→ Gate
→ Handoff / Freeze
```

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
