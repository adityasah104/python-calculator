# Code Generation Summary

## Files Created

- `calculator.py` — core arithmetic functions (`add`, `subtract`, `multiply`, `divide`) plus `calculate` dispatcher and `main` CLI entry point.
- `test_calculator.py` — 15 unit tests covering happy path and error/edge cases for all operations and the CLI.

## Key Implementation Decisions

- Integer-only arithmetic using Python `int`; division uses floor division (`//`) returning `int`.
- Errors (division by zero, unknown operator, malformed operands) return `None` from `calculate`/`divide` rather than raising; the CLI translates `None` into a stderr message and non-zero exit code.
- No external dependencies; standard library only (`sys`).
- CLI parses exactly three positional arguments: `<operand> <operator> <operand>`.

## Test Coverage Summary

- 15 tests, all passing (0.02s).
- Happy path + at least two error/edge cases per operation.
- CLI tests cover success, division by zero, and bad argument count.

## Deviations from Plan

- Test runner command uses `python3.11 -m pytest` instead of `python -m pytest` because the environment's default `python` is unavailable and `python3` (3.14) lacks pytest; pytest 8.2.0 is installed for Python 3.11.
- No `source-manifest.json` written (zero-Unit express scope).
