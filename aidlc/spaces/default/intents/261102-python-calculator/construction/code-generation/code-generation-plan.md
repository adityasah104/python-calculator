## Summary

- Builds: A Python CLI calculator supporting +, -, *, / on integers, returning None on errors
- Touches: calculator.py, test_calculator.py
- Tests: ~12 requirement-driven unit tests (happy path + error cases per operation)

## Testing Contract

```json
{
  "version": 1,
  "methodology": "test-after",
  "source": "org",
  "ordering": "implement each applicable testable layer, then write and run that layer's tests.",
  "scope": "express",
  "test_strategy": "minimal",
  "project_type": "greenfield",
  "applicable_notes": [
    {
      "layer": "org",
      "text": "We treat tests as a first-class deliverable in every Bolt. The specific\nmethodology (TDD, BDD, ATDD, or classic test-after) is affirmed at\npractices-discovery and recorded in `team.md` under this heading with explicit\n`Methodology` and `Ordering` fields; Code Generation resolves those fields\nindependently from coverage, tooling, and scope notes.\n\nWhen no posture has been affirmed, our default per scope is:\n- **Methodology**: test-after\n- **Ordering**: implement each applicable testable layer, then write and run\n  that layer's tests.\n- `mvp`, `enterprise`, `feature`, `infra`, `classic` add an 80% line-coverage\n  floor and CI execution before merge.\n- `bugfix`, `security-patch` add a targeted regression for the specific\n  bug/vulnerability and require the existing suite to remain green.\n- `express` uses the Minimal strategy: requirement-driven unit tests (one per\n  requirement, with a happy-path floor per component); existing tests remain\n  green.\n- `poc`, `refactor`, `workshop` add no extra new-test floor and require the\n  existing suite to remain green.\n\nThe active `Test Strategy` still applies in every scope and determines test\nvolume/types. Scope floors are additive; they never reduce or replace the\nselected strategy.\n\nBuild and Test verifies defined coverage floors and affirmed quality targets;\nthey may not be weakened to make a step pass.\n\nAffirm a stricter posture in `team.md` if the team commits to one."
    }
  ],
  "obligations": {
    "strategy": "minimal",
    "strategy_volume": [
      "One verifiable test per requirement at the narrowest effective level.",
      "At least one happy-path unit test per component.",
      "Unit tests are the default; a bugfix/security scope floor may require an integration or E2E regression when that is the narrowest level that reproduces the defect."
    ],
    "scope_floor": [
      "Keep the existing test suite green.",
      "This scope adds no extra new-test floor beyond the selected test strategy."
    ],
    "combination_rule": "Apply every selected-strategy obligation and every scope-floor obligation; neither replaces the other, and a targeted scope regression may add the narrowest necessary test type beyond the strategy default."
  },
  "plan_profile": {
    "methodology": "test-after",
    "runner_step": "Bootstrap the minimal test runner/configuration and record the exact unit-scoped command.",
    "runner_ready_before_first_test": true,
    "testable_layers": [
      "Data model / database behavior",
      "Repository / data access",
      "Business logic",
      "API / endpoint",
      "Frontend behavior"
    ],
    "steps": [
      "Project structure and production configuration skeleton.",
      "Bootstrap the minimal test runner/configuration and record the exact unit-scoped command.",
      "Data model / database behavior - implement.",
      "Data model / database behavior - write and run its tests after implementation.",
      "Repository / data access - implement.",
      "Repository / data access - write and run its tests after implementation.",
      "Business logic - implement.",
      "Business logic - write and run its tests after implementation.",
      "API / endpoint - implement.",
      "API / endpoint - write and run its tests after implementation.",
      "Frontend behavior - implement.",
      "Frontend behavior - write and run its tests after implementation.",
      "Environment/build configuration.",
      "Documentation and traceability."
    ]
  },
  "input_sha256": "sha256:6cb23162168334768ff8f29699669845616670119c9eb58bf9bb05af6fefd3de",
  "contract_sha256": "sha256:283a836cf0757ed2efa4b5dd3135f3986eb59880b3017f4ba87a685cfebedfdb"
}
```

## Plan Steps

- [x] Step 1: Project structure skeleton — create `calculator.py` and `test_calculator.py` at workspace root.
- [x] Step 2: Bootstrap the minimal test runner — ensure `pytest` is available and record the exact unit-scoped command: `python -m pytest test_calculator.py -v`.
- [x] Step 3: Business logic — implement core functions in `calculator.py`: `add`, `subtract`, `multiply`, `divide` (return `None` on division by zero) and a `calculate(operand1, operator, operand2)` dispatcher returning `None` on invalid input.
- [x] Step 4: Business logic — write and run unit tests in `test_calculator.py` covering happy path and at least two error/edge cases per operation (FR1.1–FR1.4, FR3.1, FR3.2).
- [x] Step 5: CLI / endpoint layer — implement `main()` in `calculator.py` parsing `sys.argv` as `<operand> <operator> <operand>`, printing the result or an error message to stderr with non-zero exit on `None`.
- [x] Step 6: CLI — write and run tests covering valid invocations and error cases (FR2, FR4).
- [x] Step 7: Documentation and traceability — finalize docstrings and `traceability.json`.

## Traceability

| Plan Step | Requirement |
|-----------|-------------|
| Step 3 | FR1.1, FR1.2, FR1.3, FR1.4, FR3.1, FR3.2 |
| Step 5 | FR2, FR2.1, FR4.1, FR4.2 |
| Step 4, 6 | NFR2 |
