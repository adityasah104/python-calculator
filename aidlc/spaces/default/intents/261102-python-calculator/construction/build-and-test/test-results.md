# Test Results

## Build Status

- **Success** — `python3.11 -m py_compile calculator.py` exited 0.

## Test Results

- **Total**: 15
- **Passed**: 15
- **Failed**: 0
- **Skipped**: 0
- **Duration**: 0.02s

## Test Breakdown

| Test | Status |
|------|--------|
| test_add | PASSED |
| test_add_negative | PASSED |
| test_subtract | PASSED |
| test_subtract_negative_result | PASSED |
| test_multiply | PASSED |
| test_multiply_by_zero | PASSED |
| test_divide | PASSED |
| test_divide_by_zero | PASSED |
| test_divide_truncates | PASSED |
| test_calculate_add | PASSED |
| test_calculate_unknown_operator | PASSED |
| test_calculate_malformed | PASSED |
| test_cli_success | PASSED |
| test_cli_division_by_zero | PASSED |
| test_cli_bad_args | PASSED |

## Coverage Report

Minimal strategy — no coverage floor beyond the selected strategy for express scope. No coverage tooling configured.

## Failure Details

None — all tests passed.

## Target Verification Matrix (Finalized)

| Target ID | Source | Expected | Actual | Evidence | Owning Stage | Verdict |
|-----------|--------|----------|--------|----------|--------------|---------|
| BUILD-1 | build-instructions.md | py_compile succeeds | Success | `python3.11 -m py_compile calculator.py` exit 0 | build-and-test | Met |
| TEST-1 | unit-test-instructions.md | 15 tests pass | 15 passed, 0 failed | `python3.11 -m pytest test_calculator.py -v` | build-and-test | Met |
| NFR1 | requirements.md §NFR1 | Python 3, stdlib only | No external deps | code review + py_compile | build-and-test | Met |
| NFR2 | requirements.md §NFR2 | Happy path + ≥2 error cases per op | 15 tests covering all ops | pytest output | build-and-test | Met |
| NFR3 | requirements.md §NFR3 | Runnable as script | `python calculator.py ...` works | CLI tests pass | build-and-test | Met |
| CI-1 | Testing Contract | Run selected tests in CI before merge | N/A | Plan runs no CI Pipeline | N/A | N/A |