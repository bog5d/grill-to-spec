# PROJECT ROADMAP — <Project Name>

> 生命周期导航，不取代 SPEC / TASKS / ACCEPTANCE / runtime state。

## Project Goal

<最终产品目标>

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
- 只有 PROJECT_COMPLETE=true 才能整体封箱
- 新 Phase 只对新增 P0 做增量 Grill

## Backlog / Future Phases

- ...
