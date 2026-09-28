# Grill to Spec

**Grill → Converge → Spec → Spike → Plan → Tasks → SCP Gate**

一个面向 AI 开发的需求澄清与交付前置方法：先把需求问清楚，再形成可开发、可验收、可交接的 Spec；只有真正存在技术未知时才做 Spike。

## 解决什么问题

很多 AI 开发失败，不是代码能力不足，而是需求还没说清楚就开始写代码。本仓库负责把“脑子里的想法”变成“任何 AI/开发者都能接手的施工文件”。

## 核心原则

1. 不直接开发，先 Grill。
2. 每轮只问 1–3 个真正改变架构/交付的问题。
3. 问题分 P0 / P1 / P2：P0 必须回答，P1 可显式假设，P2 进入 backlog，不阻塞交付。
4. 持续检查 GCCSEG：Goal / Context / Capability / State / Evidence / Gate。
5. 需求足以施工时必须主动停止追问，进入 Converge。
6. 先形成“足够靠谱”的 Spec，不追求文档完美。
7. 只有技术未知会改变方案时才做 Spike；Spike 必须时间盒化。
8. 工程阶段遵守 SCP v3.4：可靠、复用、迁移、AI 稳定、积木化、黑盒化。

## 最短用法

把下面这句话交给任意 AI：

> 请读取本仓库 `START_HERE.md`，进入 Grill to Spec 模式。先不要开发，逐轮把需求问清楚；达到收敛门后生成完整 Spec、Architecture、Plan、Tasks。只有重大技术未知才提出 Spike。

## 目录

- `START_HERE.md`：AI 入口
- `GRILL.md`：追问协议
- `CONVERGE.md`：何时停止问
- `GCCSEG.md`：需求完整性检查
- `SPEC_LIFECYCLE.md`：从想法到施工的生命周期
- `SCP-v3.4.md`：工程原则
- `templates/`：标准产出模板
- `examples/`：真实跑通过的例子
- `HANDOFF.md`：接力说明

## 当前版本

V0.1 — dogfood 版本。第一例：`仓颉 Teams Channel`。
