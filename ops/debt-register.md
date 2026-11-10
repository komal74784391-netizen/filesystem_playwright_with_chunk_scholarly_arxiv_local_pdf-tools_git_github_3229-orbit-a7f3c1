# Engineering Debt Register

Hand-maintained by the platform team. This register is a curated view of
outstanding `TODO(owner)` annotations and is **not** an exhaustive mirror of
the source tree. Last reconciled at release **v2.4.0**.

Scope: annotations that occupy their own line under `src/` or `tools/` and
carry an owner and a note. Vendored and third-party trees are not tracked;
inline trailing annotations and owner-less TODO comments are not tracked.

| ID | File | Line | Note |
|----|------|------|------|
| DB-001 | src/orbit/engine/core.py | 12 | TODO(dmarino): unify the adaptive CFL guard used by both integrators. |
| DB-002 | src/orbit/engine/core.py | 26 | TODO(hsato): tighten this once the TVD limiter lands. |
| DB-003 | src/orbit/engine/core.py | 35 | TODO(jkolb): report the substep count through the telemetry hook. |
| DB-004 | src/orbit/engine/core.py | 44 | TODO(pnair): take the halo width from the mesh descriptor. |
| DB-005 | src/orbit/engine/core.py | 46 | TODO(dmarino): support periodic and reflective boundaries in one pass. |
| DB-006 | src/orbit/engine/core.py | 56 | TODO(jkolb): drop the scalar path once the vectorised kernel is default. |
| DB-007 | src/orbit/engine/parser.py | 8 | TODO(mokonkwo): support nested section overrides in the loader. |
| DB-008 | src/orbit/engine/parser.py | 33 | TODO(trenner): validate that section names are unique. |
| DB-009 | src/orbit/engine/parser.py | 42 | TODO(sbrann): emit a structured error with the offending line number. |
| DB-010 | src/orbit/engine/parser.py | 49 | TODO(blundqvist): quote values that contain whitespace. |
| DB-011 | src/orbit/engine/parser.py | 51 | TODO(mokonkwo): drop the trailing newline for round-trip parity. |
| DB-012 | src/orbit/engine/planner.py | 13 | TODO(dmarino): clamp the refined level to the configured maximum. |
| DB-013 | src/orbit/engine/planner.py | 18 | TODO(trenner): add anisotropic refinement along dominant gradients. |
| DB-014 | src/orbit/engine/planner.py | 23 | TODO(mokonkwo): return a diff plan instead of a full snapshot. |
| DB-015 | src/orbit/engine/scheduler.py | 21 | TODO(pnair): guard against duplicate job names at insertion time. |
| DB-016 | src/orbit/engine/scheduler.py | 25 | TODO(jkolb): raise SchedulerError instead of silently skipping. |
| DB-017 | src/orbit/engine/scheduler.py | 32 | TODO(hsato): return a sentinel job so callers can pattern-match. |
| DB-018 | src/orbit/engine/scheduler.py | 37 | TODO(sbrann): preserve deterministic order across worker pools. |
| DB-019 | tools/bench/run_bench.py | 9 | TODO(sbrann): warm up the JIT before collecting samples. |
| DB-020 | tools/bench/run_bench.py | 19 | TODO(dmarino): store results in the shared benchmark database. |
| DB-021 | tools/cli/io_utils.py | 13 | TODO(jkolb): read defaults from the packaged profile instead. |
| DB-022 | tools/cli/io_utils.py | 20 | TODO(hsato): pretty-print only when the stream is a tty. |
| DB-023 | tools/cli/io_utils.py | 26 | TODO(blundqvist): include the estimated memory footprint. |
| DB-024 | tools/cli/main.py | 11 | TODO(sbrann): split the argument groups into a dedicated module. |
| DB-025 | tools/cli/main.py | 24 | TODO(dmarino): validate the schema version before planning. |
| DB-026 | tools/cli/main.py | 27 | TODO(pnair): return a distinct exit code for validation failures. |
| DB-027 | tools/cli/main.py | 32 | TODO(trenner): support a --dry-run flag that skips IO entirely. |
| DB-028 | tools/cli/main.py | 39 | TODO(mokonkwo): wire up structured logging before the first file is read. |
