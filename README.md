# Grill to Spec

**Grill → Converge → Spec → Architecture → Project Roadmap → Phase → Plan → Tasks → SCP Gate**

一个面向 AI 开发的需求澄清与持续交付方法：先把需求问清楚，再形成可开发、可验收、可交接、可持续推进的施工体系。

## 解决什么问题

AI 开发常见两类失败：
1. 需求没说清楚就开始写代码；
2. 某个 Phase 做完后，AI误以为整个项目结束。

本仓同时解决这两类问题。

## 核心原则

1. 不直接开发，先 Grill。
2. 每轮只问 1–3 个真正改变架构/交付的问题。
3. P0 必须解决；P1 可显式假设；P2 进 backlog。
4. 持续检查 GCCSEG。
5. 足够施工时主动 Converge。
6. 形成 Spec + Architecture + **Project Roadmap** + Plan + Tasks。
7. **Phase completion ≠ Project completion。**
8. 只有重大技术未知才做 Spike。
9. 工程阶段遵守 SCP v3.4。
10. 非终态自动推进，不因阶段汇报停。

## 最短用法

> 请读取本仓库 `START_HERE.md`，进入 Grill to Spec 模式。先不要开发；逐轮澄清需求。收敛后生成 Spec、Architecture、PROJECT_ROADMAP、Plan、Tasks。开发阶段必须按 Roadmap 自动推进；只有 PROJECT_COMPLETE=true 才能整体封箱。

## 目录

- `START_HERE.md`：AI 入口
- `GRILL.md`：追问协议
- `CONVERGE.md`：停止追问规则
- `GCCSEG.md`：需求完整性
- `SPEC_LIFECYCLE.md`：完整生命周期
- `PROJECT_ROADMAP.md`：项目阶段导航协议
- `SCP-v3.4.md`：工程原则
- `docs/ESCALATION.md`：少问 / 升级纪律
- `templates/PROJECT_ROADMAP.md`：项目 Roadmap 模板
- `templates/`：其他标准产出
- `examples/`：真实案例
- `HANDOFF.md`：方法论仓交接

## 当前版本

V0.2-dogfood — 第一真实案例：`仓颉 Teams Channel`。
