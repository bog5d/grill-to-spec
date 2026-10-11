# SCP v3.7｜可靠·复用·迁移·AI稳定·积木黑盒化·Harness原生

> 本文件是工程原则的权威版本。GCCSEG 是本仓自定义框架，并非外部行业标准。小任务按风险分级；有状态、长时、多执行器或可恢复需求的工程必须使用完整 Harness。详细规范见 `HARNESS.md`，机器检查见 `contracts/` 与 `scripts/`。

## 目标与适用
构建高可用、可审计、可恢复、可迁移的系统；用户、部门、公司、设备、模型、路径、账户不得硬编码进 Kernel。单部门可用→跨部门复用→跨公司迁移。简单、无持久状态、低风险的小改动只需遵守安全与回归要求，不强制建设独立 Harness。任何模块都应可被共享 Harness 管理，不要求每个模块自建 Harness。

## 1. 复用优先
开工前依次扫描：已验收内部组件/Skill/Pack/Adapter；GitHub及成熟开源社区；成熟标准/商业方案的架构和数据模型；最后自研。中大型任务输出 reuse matrix：候选、成熟度、活跃度、License、依赖、迁移性、接入成本、风险、复用方式和取舍证据。先复用代码/Schema/协议/测试/算法，经 Adapter 隔离；不得以“自己可控”为理由默认重写。小任务按比例简化。

## 2. 架构分层
先分类 Kernel、Department Pack、Company Extension。公司特例不入 Kernel；跨项目复用并经 Gate 后逐级上提。60%通用/40%扩展仅为方向。KISS、YAGNI、显式优于隐式。

## 3. 角色与持续执行
Planner/Executor/Reviewer 职责分离；可由不同 AI 或同一 AI 的独立阶段承担，但执行者自报不算独立验收。已有 Cursor、dsh、Hermes、MiniMax 等按真实可用性和成本策略派工，禁止硬编码具体模型。非终态且无须人工裁决时自动推进；不能靠聊天会话存活保证持续性，必须具备外部唤醒、持久队列、租约与恢复证据。平台支持时长任务10–15分钟检查活性；不能设提醒的平台必须由外部守护/调度承担，不得虚称已设置。

## 4. Harness 原生 GCCSEG
对中大型、自主运行、异步、调度或可恢复任务，必须明确：
- Goal：目标、非目标、可验证验收条件。
- Context：事实来源、版本、时效、适用范围；区分 CURRENT/HISTORICAL/INFERRED/UNKNOWN。
- Capability：生效配置、真实执行路径、权限、额度、依赖、能力级别；探测必须使用正式路径及参数。
- State：持久状态、合法转移、心跳/租约、停滞、恢复、next_action、幂等。
- Evidence：来源、事件时间、采集时间、对象、配置/代码版本、命令/退出码、产物、校验；证据须与结论对应。
- Gate：独立需求级验收、阻断条件、失败恢复与阶段晋级。

运行闭环：Intent/Spec → Execute → Observe → Evaluate → Correct → Verify → persist → next_action。完整契约见 `HARNESS.md`。

## 5. 证据可信度与反误判
历史日志可用于追溯，不能单独证明当前故障；进程存在、日志刷新、文件修改不能单独证明有效施工；CLI PONG 不等于 GM 自主派工。关键健康/准入/下线/完成判断必须核对对象、时效、当前生效配置、证据类别、结论适用范围。证据不足返回 UNKNOWN/INSUFFICIENT_EVIDENCE，禁止编造事实或擅自下线。基线对照必须同方法、同范围、同解析，先核实测试语义再修改断言。

## 6. 模块契约与黑盒封存
单一职责、故障边界、输入输出错误 Schema 版本配置依赖明确。路径、模型、账户、阈值、数据源、通知配置化；优先 Adapter/Pack/Config，不堆核心 if/else。功能、异常、安全、迁移、性能和回归 Gate 通过后封存；只因契约失败、Bug、安全、性能、依赖失效或扩展失败解封，修改后重新验收。

## 7. 能力生长
系统识别高频、耗时、易错、高价值、稳定且可迁移的工作，生成 Capability Candidate；工作→发现→候选卡→人类确认→Grill/Spec→批准→开发→试运行→Gate→Extension/Pack/Kernel。普通成员优先选择题，Owner 再回答 3–5 个关键 Grill；通常重复 2–3 次或首次明显高价值时触发。能力晋级须提供真实复用证据，不得仅靠 AI 主张。

## 8. AI 确定性与安全
代码/规则/状态机/Schema 高于 AI 自由判断。权限、金额、状态、删除、发送、外部写由确定性机制裁决；AI 用于语义和候选发现，输出固定 Schema 校验。Prompt、模型、参数、输出格式版本化。高风险删除/覆写/外发/外部写默认 dry-run，提供目标、数量、Diff、影响、回滚；需要人工授权时不得绕过。

## 9. 测试、部署与交付
开工 validate_environment()；修 Bug 必补回归；一次一改立即验证。测试代码同等审查。区分五级：①CLI 可调用 ②真实施工 ③GM 自主派工 ④故障切换 ⑤会话结束后无人值守接棒；不得跨级宣布 PASS。代码提交≠合并≠部署≠真实运行。交付附命令、退出码、Evidence、部署版本、状态变化、next_action；不合格 Gate 不得伪称完成。

## 10. 交接与节奏
改代码前读当前项目的权威入口、README、SPEC、ARCHITECTURE、ADR、测试、配置、持久状态及本仓规则；若项目采用 GM，则额外读取其 GM 任务与状态契约，不把特定私有仓硬编码为所有项目的依赖。任务有 Goal、Non-goal、Acceptance、依赖、风险、Owner、状态、next_action；多阶段 Project Roadmap 持续推进，Phase PASS 不等于 Project COMPLETE。真实设备用于必要 Real Environment Gate，不要求日常开发都依赖设备。顺序：复用扫描→当前事实→Spec/Acceptance→分层→派工→实测→Evidence→独立 Gate→自动接棒。

## 版本治理
任何规则修改须 PR、版本记录和相应测试；不得仅修改文字而宣称“代码强制”。机器可执行检查是底线，语义性要求由独立 Reviewer 审核。