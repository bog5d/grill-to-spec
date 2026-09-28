# PROJECT ROADMAP Protocol

## Why

Spec / Architecture / Tasks 解决“怎么施工”，但还需要一层回答：

- 整个项目分几期
- 当前在哪一期
- 当前 Child 是什么
- Phase 完成后去哪
- 什么时候才允许宣称整个项目完成

没有这一层，AI 很容易把“某个 Phase PASS”误判成“项目完成”。

## Hard Rule

**Phase completion ≠ Project completion。**

项目只有在 PROJECT_ROADMAP 明确：

`PROJECT_COMPLETE = true`

时才能整体封箱。

## Required Fields

每个多阶段项目至少维护：

```text
PROJECT_COMPLETE = false
CURRENT_PHASE = ...
CURRENT_STATUS = ...
CURRENT_CHILD = ...
NEXT_ACTION = ...
```

并列出：
- Project Goal
- Phase Map
- 每个 Phase 的 Status / Goal / Exit Criteria
- Next on PASS
- Backlog / future phase（若有）

## Auto-Advance

- Child PASS → 下一 Child
- Phase PASS → 读取 Roadmap
- 有下一 Phase → 形成/更新下一 Phase Parent + Tasks 后继续
- 没有明确下一 Phase → 检查 BACKLOG / OPEN_QUESTIONS / product goal
- 只有确认产品目标已完成，才设置 PROJECT_COMPLETE=true

阶段汇报不是停止条件。

## Incremental Grill

进入新 Phase 时：
- 已验收范围不得重新 Grill
- 如果新 Phase 有真正 P0 级边界未知，只对新增范围做增量 Grill
- P1/P2 记录假设或 backlog，不阻塞

## Truth Boundary

PROJECT_ROADMAP 是**导航层**，不是第二事实源：
- Product boundary → SPEC
- Implementation work → TASKS / Parent
- Acceptance → ACCEPTANCE / Evidence
- Runtime truth → 项目自己的状态系统

Roadmap 只指向它们并声明生命周期位置。
