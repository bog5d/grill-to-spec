# Adopt SCP v3.7

1. Classify the change L0 (small), L1 (engineering), or L2 (autonomous) using HARNESS.md.
2. For L1/L2, read README.md, START_HERE.md, SCP-v3.7.md, HARNESS.md and the local project contract.
3. Declare GCCSEG in a versioned JSON artifact; validate using `python scripts/check_gccseg.py path/to/task.json`.
4. Record real evidence, not model claims; independently review semantic claims and actual execution.
5. Add the checker and regression tests to each project's own CI. This repository cannot automatically block merges elsewhere.
6. For L2, prove CLI, real execution, autonomous dispatch, failover, and unattended handoff separately.
7. Pin the rule version to a reviewed tag or commit, and upgrade through a controlled PR.

A plain URL in a prompt is a reference, not proof that an agent fetched or complied with it. If unavailable, report the missing rule source and do not claim compliance.
