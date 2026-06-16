# eval-target-repo

A deliberately tiny Python "notes" service used as the **target** for the
Week-3 Code Review Agent. The `main` branch is a clean baseline. Each
`pr/*` branch introduces **one known class of issue** so we can measure
whether the reviewer's specialist agents catch it.

| Branch | Specialist it exercises | Planted issue(s) |
|---|---|---|
| `pr/security-sql-injection` | Security | f-string SQL injection + hardcoded secret |
| `pr/quality-refactor` | Code quality | mutable default arg, duplicated logic, dead code, bare `except` |
| `pr/test-gap` | Test gaps | new pure function shipped with no test |

Ground truth for scoring lives in [`SEEDED_BUGS.md`](./SEEDED_BUGS.md).

## Layout

```
app/
  db.py       # sqlite connection + schema
  notes.py    # CRUD business logic (parameterized — clean)
  utils.py    # small pure helpers
tests/
  test_notes.py
  test_utils.py
```

## Run tests

```bash
pip install -r requirements.txt   # only pytest
pytest -q
```

## Creating the PRs on GitHub

This is its own standalone git repo. Push it to a GitHub repo of your own,
then open a PR for each `pr/*` branch against `main`:

```bash
git remote add origin git@github.com:<you>/eval-target-repo.git
git push -u origin main
git push origin pr/security-sql-injection pr/quality-refactor pr/test-gap
# then open 3 PRs in the GitHub UI (or with: gh pr create --base main --head <branch>)
```
