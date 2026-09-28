# HANDOFF — Grill to Spec

## 当前状态

方法论已完成第一次真实 dogfood，并吸收两个关键改进：
1. 少问 / 升级纪律：`docs/ESCALATION.md`
2. 项目生命周期导航：`PROJECT_ROADMAP.md`

当前版本：**V0.2-dogfood**。

## 新项目标准交付

Converge 后应生成：

- INTENT
- REQUIREMENTS
- NON_GOALS
- OPEN_QUESTIONS
- SPEC
- ACCEPTANCE
- ARCHITECTURE
- **PROJECT_ROADMAP**
- PLAN
- TASKS
- BACKLOG
- SPIKES（仅必要时）

## 硬规则

**Phase completion ≠ Project completion。**

开发 AI 必须先读产品仓 `PROJECT_ROADMAP.md`。只要
`PROJECT_COMPLETE=false`，就继续 Current Child / Next Phase。

## 第一真实案例

`bog5d/cangjie-teams-channel`

该案例暴露并验证了 Roadmap 层的必要性：仅有 SPEC / ARCHITECTURE / PLAN / TASKS 时，
阶段完成容易被误判成项目完成。

后续继续用真实项目 dogfood，再迭代方法论。
