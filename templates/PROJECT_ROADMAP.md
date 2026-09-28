# PROJECT ROADMAP

> 生命周期总导航：说明项目一共分几期、当前在哪一期、下一步是什么、什么时候才算整个项目完成。

## Project State

- PROJECT:
- PROJECT_STATUS: ACTIVE
- PROJECT_COMPLETE: false
- CURRENT_PHASE:
- CURRENT_CHILD:
- NEXT_AFTER_PASS:
- LAST_VERIFIED_MAIN:

## Phase Map

| Phase | Goal | Status | Completion Gate | Next |
|---|---|---|---|---|
| Phase 1 |  | PLANNED |  |  |
| Phase 2 |  | PLANNED |  |  |
| Phase 3 |  | PLANNED |  |  |

## Current Phase Progress

- Child A:
- Child B:
- Child C:

## Lifecycle Rules

1. Phase PASS ≠ Project Complete.
2. 当前 Phase PASS 后，如 PROJECT_COMPLETE=false，必须自动进入下一 Phase，不得因阶段汇报停机。
3. 只有 PROJECT_COMPLETE=true 且 Project Completion Gate 有 Evidence，才允许整体封箱。
4. 新 Phase 开始前，基于既有 SPEC / ARCHITECTURE / PLAN / BACKLOG 建立该 Phase 的 Parent Work、Child WPs、Acceptance、Evidence。
5. 非架构级未知不重新 Grill；P1/P2 写显式假设继续。
6. Roadmap 只做生命周期导航，不替代运行时状态源。

## Project Completion Gate

- 所有必须 Phase DONE
- 最终能力与最新 SPEC 一致
- 最终 Acceptance 有独立 Evidence
- 无阻塞性安全/一致性问题
- HANDOFF 写明最终版本、HEAD、遗留项、解封条件
