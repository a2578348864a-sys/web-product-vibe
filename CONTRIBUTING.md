# Contributing

Web Product Vibe is intentionally small. Contributions should reduce ambiguity, rework or false completion claims without turning the project into a heavyweight framework.

## Good contributions

- clearer product / UX decision rules
- stronger scope-control rules
- better real-browser acceptance checks
- platform compatibility fixes
- smaller or clearer templates
- concrete examples that expose failure modes

## Avoid

- adding process only for completeness
- host-specific behavior inside the core workflow when a portable rule works
- expanding the number of artifacts without a demonstrated need
- treating a new AI/tool trend as an automatic requirement

## Before opening a PR

Run:

```bash
python tools/check_skill.py
```

If behavior changes, update `CHANGELOG.md` and the relevant docs.
