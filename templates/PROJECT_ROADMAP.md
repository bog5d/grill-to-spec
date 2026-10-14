# PROJECT ROADMAP — <Project Name>

> 生命周期导航，不取代 SPEC / TASKS / ACCEPTANCE / runtime state。

## Project Goal

<用户可观察的最终产品目标，不以局部测试/代码提交替代>

## Goal-Aligned Baseline

- 最终用户场景：
- 当前效果/基线证据：
- 工程完成率：UNKNOWN（单独衡量）
- 用户终局效果达成率：UNKNOWN（固定指标及分母后才能填百分比）
- 硬门槛及证据：
- 当前最大业务目标差距：

## Current State

```text
PROJECT_COMPLETE = false
CURRENT_PHASE = <Phase N>
CURRENT_STATUS = PLANNED | IN_PROGRESS | PASS | BLOCKED
CURRENT_CHILD = <WP>
NEXT_ACTION = <next executable action>
```

## Phase Map

### Phase 1 — <name>
Status: ...
Goal: ...
Exit Criteria:
- ...
Next on PASS: Phase 2

### Phase 2 — <name>
Status: ...
Goal: ...
Exit Criteria:
- ...
Next on PASS: ...

## Lifecycle Rule

- Child PASS → 下一 Child
- Phase PASS → 下一 Phase
- Phase completion ≠ Project completion
- 即使 Phase PASS，也必须确认它确实减少终局业务目标差距；否则列出目标漂移整改项
- 只有 PROJECT_COMPLETE=true 才能整体封箱
- 新 Phase 只对新增 P0 做增量 Grill

## Backlog / Future Phases

- ...
