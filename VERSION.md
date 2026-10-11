# SCP engineering policy versions

- v3.7 candidate: Harness-native GCCSEG, evidence integrity, autonomy acceptance levels, L0/L1/L2 complexity classification.
- v3.6: previous user-authored principle set; v3.7 retains reuse scan, Kernel/Pack/Extension, role separation, capability growth, safety, and durable handoff.
- v3.4: historical SCP-v3.4.md retained for traceability.

The default branch is the published entry after review. Production consumers should pin a commit SHA or tag for repeatability. This repository's CI checks structural fixtures only; downstream projects must integrate the gate themselves. A passing structural gate does not establish semantic correctness or unattended execution.
