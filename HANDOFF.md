# HANDOFF — Grill to Spec

## 当前状态

- 远端仓库：`bog5d/grill-to-spec`，`main` 为当前方法论真相源。
- 已完成 Grill / GCCSEG / Converge / Spec / Architecture / SCP v3.4 / 少问升级纪律。
- 已补项目生命周期层：`PROJECT_ROADMAP.md`。
- 核心硬规则：**Phase PASS ≠ Project Complete**；只有 `PROJECT_COMPLETE=true` 且 Project Completion Gate 有独立 Evidence，才允许整体封箱。
- 第一真实 dogfood：`bog5d/cangjie-teams-channel`，已按 Roadmap 进入 Phase 2。

## 标准施工产物

收敛后标准产物应包含：

- INTENT
- REQUIREMENTS
- NON_GOALS
- OPEN_QUESTIONS
- SPEC
- ACCEPTANCE
- ARCHITECTURE
- **PROJECT_ROADMAP**
- PLAN
- TASKS / Work Packages
- SPIKES（仅重大技术未知时）

## 生命周期接力

1. 先读 `PROJECT_ROADMAP.md`。
2. 找 CURRENT_PHASE / CURRENT_CHILD / NEXT_ACTION。
3. Child PASS → 同 Phase 下一 Child。
4. Phase PASS → 若 `PROJECT_COMPLETE=false`，自动进入下一 Phase。
5. 新 Phase 基于既有 SPEC / ARCHITECTURE / PLAN / BACKLOG 形成 Parent Work + Child WPs + Acceptance + Evidence。
6. 非架构级未知不重新 Grill；P1/P2 写显式假设继续。
7. 阶段汇报不是停止条件。
8. 只有 `PROJECT_COMPLETE=true` + Project Completion Gate PASS 才允许 Freeze。

## 交接原则

- 方法论仓与业务产品仓保持独立。
- Roadmap 是生命周期导航，不替代业务仓运行时状态源。
- 不因单个 WP / V1 / Phase PASS 宣称整个项目完成。
- 执行阶段继续遵守 `SCP-v3.4.md` 与 `docs/ESCALATION.md`。
