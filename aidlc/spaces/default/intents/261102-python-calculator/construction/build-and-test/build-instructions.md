# Build Instructions

## Dependency Installation

No external dependencies required. The calculator uses only the Python standard library plus `pytest` for testing.

```bash
python3.11 -m pip install pytest
```

## Environment Setup

No environment variables, configuration files, or local services required.

- Python 3.11+ (available at `/opt/homebrew/opt/python@3.11/bin/python3.11`)
- pytest 8.2.0 (installed for Python 3.11)

## Build Commands

No compilation or bundling required — Python is interpreted.

```bash
# Verify syntax
python3.11 -m py_compile calculator.py
```

## Build Verification

```bash
python3.11 -m py_compile calculator.py && echo "Build OK"
```

## Troubleshooting

- If `python` is unavailable, use `python3.11` explicitly.
- If pytest is not installed for Python 3.11, run `python3.11 -m pip install pytest`.
- The default `python3` (3.14) does not have pytest installed; always use `python3.11`.