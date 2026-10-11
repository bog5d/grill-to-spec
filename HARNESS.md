# Harness / GCCSEG 强制设计契约

## 分级
- L0 轻量：单文件、小修复、无异步持久状态、低风险。只要求目标、变更范围、回归和安全；无需创建独立 Harness。
- L1 工程：跨模块、多人/多 Agent 或可发布功能。必须声明 GCCSEG，复用项目已有状态/Evidence/Gate。
- L2 自治：长时运行、后台调度、故障恢复、外部写入、多执行器。必须具备持久状态、租约、幂等、证据验证、独立 Gate、故障注入与真实无人值守验收。

## GCCSEG
G Goal：明确成功条件和不可做的事。
C Context：记录来源、event_at、collected_at、版本、CURRENT/HISTORICAL/INFERRED/UNKNOWN。历史记录只证明历史；AI 叙述不自动变事实。
C Capability：从当前生效配置获取真实路径、参数、环境、工作目录、权限及模型；替代 CLI 结果不可用于否定正式入口。
S State：状态转移必须合法，RUNNING 无执行器/无租约/无进展须进入恢复路径；区分 alive、productive、blocked、unknown；任务进展以有效产物与 Gate 为准。
E Evidence：至少 subject_id、source、event_at、collected_at、config_version、code_version、claim、observation、validation_result；命令、退出码、artifact 在适用时记录。检查对象一致性、时效、独立性与完整性。
G Gate：Reviewer 按需求级行为判断，不绑定特定执行器的实现细节；CLI_READY、TASK_EXECUTED、AUTONOMOUS_DISPATCHED、FAILOVER_VERIFIED、UNATTENDED_HANDOFF_VERIFIED 分别取证。

## 防误判回归
1. 旧 quota 不得永久封锁当前可用执行器。
2. 陈旧 crash 日志不能单独宣布当前崩溃。
3. 错误 shim 失败不能否定生效配置入口成功。
4. 未提交文件不等于阻塞。
5. one-shot watchdog 正常退出不等于服务死亡。
6. 进程/日志活跃不等于任务进展。
7. main 与分支测试基线须同法比对，不能静默忽略新增失败。
8. RUNNING 无活执行器时必须有可验证的恢复路径。
9. 任何重大结论缺足够证据应为 UNKNOWN，不能自动降级成 FAIL。

## 实施约束
此仓是规范与合规工具，不是各业务系统的第二个运行控制面。业务仓通过版本化规则、JSON Schema、CI 与 Reviewer 复用；不复制一套 GM。机器 Gate 只能保证可形式化的规则，语义正确性必须由真实实验和独立复核支持。