# Unit Test Instructions

## Test Framework

- Framework: pytest
- Python: 3.x (standard library + pytest)
- No additional dependencies beyond pytest.

## How to Run This Unit's Tests

Exact command (run from workspace root):

```
python3.11 -m pytest test_calculator.py -v
```

This command is scoped to `test_calculator.py` only. Do not run a bare `pytest` or `python -m pytest` (project-wide) — Build and Test executes every unit's commands, and an unscoped command would rerun the whole suite once per unit.

## Expected Coverage Targets

- Minimal strategy: one verifiable test per requirement at the narrowest effective level, plus at least one happy-path unit test per component.
- At least two error/edge cases per operation (division by zero, malformed input, unknown operator).
- No coverage floor beyond the Minimal strategy for this express scope.

## Mocking / Stubbing Guidance

- No external services or I/O to mock; the calculator is pure functions plus a CLI entry point.
- For CLI tests, use `capsys` / `monkeypatch` to capture stdout/stderr and simulate argv.

## Test Data Management

- Inline small integers in test functions; no fixtures or external data files required.
- Keep tests independent and order-independent.
