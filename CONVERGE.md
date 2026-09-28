# CONVERGE — 停止追问规则

满足以下条件即可停止 Grill：

1. Goal 可以用一句话说清楚。
2. 关键用户与第一使用场景明确。
3. 核心输入/输出明确。
4. 关键数据边界与保密边界明确。
5. GCCSEG 六项不存在未回答的 P0。
6. 当前首个 Phase 的成功 Gate 明确。
7. Non-goals 已明确，避免范围继续膨胀。
8. 剩余问题均可降级为显式假设、Backlog 或 Spike。
9. 如果项目天然是多阶段，已经能画出最小 Phase Map，并明确“下一阶段存在但不属于当前施工范围”的内容。

## 收敛动作

先输出“我理解的最终需求”，让用户最后纠偏；随后生成标准施工文件：

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

其中 `PROJECT_ROADMAP.md` 必须明确：

```text
PROJECT_COMPLETE = false
CURRENT_PHASE = ...
CURRENT_CHILD = ...
NEXT_ACTION = ...
```

以及每个已知 Phase 的 Goal / Status / Exit Criteria / Next on PASS。

## 生命周期规则

**Converge 只代表“足够安全地开始施工”，不代表项目已经定义到永久终局。**

- Child PASS → 下一 Child。
- Phase PASS → 回到 PROJECT_ROADMAP。
- PROJECT_COMPLETE=false 且存在下一 Phase → 自动进入下一 Phase。
- 新 Phase 只有新增 P0 才做增量 Grill；已验收范围不重新 Grill。
- 只有 PROJECT_COMPLETE=true 且 Project Completion Gate 有 Evidence，才允许整体封箱。

注意：收敛不是“所有问题都解决”，而是“已经足够安全地进入当前 Phase 施工，并且知道当前 Phase 完成后往哪里走”。
