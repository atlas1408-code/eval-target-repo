# Seeded bugs — ground truth for the Code Review Agent eval

Each `pr/*` branch introduces exactly the issues listed here. Use this as the
expected-findings key when scoring the reviewer's hit rate (Phase 8 eval).

---

## `pr/security-sql-injection` → Security agent

File: `app/search.py`

| # | Issue | Severity | Location | Expected finding |
|---|---|---|---|---|
| S1 | SQL injection via f-string in `WHERE` clause | critical | `search_notes`, the `query = f"... LIKE '%{term}%'"` line | Should flag string-interpolated SQL; recommend parameterized query |
| S2 | Hardcoded secret / API token committed in source | high | module-level `EXPORT_API_TOKEN = "sk-..."` | Should flag hardcoded credential; recommend env var / secret store |

## `pr/quality-refactor` → Code-quality agent

File: `app/digest.py`

| # | Issue | Severity | Location | Expected finding |
|---|---|---|---|---|
| Q1 | Mutable default argument `tags=[]` | medium | `build_digest(..., tags=[])` | Should flag shared mutable default; recommend `None` sentinel |
| Q2 | Duplicated formatting logic (copy-pasted block) | low | the two near-identical title/body format blocks | Should flag duplication; recommend extracting a helper |
| Q3 | Dead/unreachable code after `return` | low | lines after the early `return` in `build_digest` | Should flag unreachable code |
| Q4 | Bare `except:` swallowing all errors | medium | the `try/except` around the count step | Should flag bare except; recommend catching specific exception |

## `pr/test-gap` → Test-gap agent

File: `app/stats.py` (no matching `tests/test_stats.py` added)

| # | Issue | Severity | Location | Expected finding |
|---|---|---|---|---|
| T1 | New public pure function shipped with zero tests | medium | `reading_time_minutes` / `note_stats` | Should flag missing test coverage for new module |
