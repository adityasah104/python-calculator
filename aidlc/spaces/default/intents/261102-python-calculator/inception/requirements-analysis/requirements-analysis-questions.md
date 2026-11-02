# Requirements Analysis Questions

## Q1. [Product] Supported operations

Which arithmetic operations should the calculator support?

A. Basic only: add, subtract, multiply, divide
B. Basic plus modulo (%) and exponentiation (**)
C. All of the above plus square root and absolute value
D. Full scientific: trigonometry, logarithms, constants (pi, e)
X. Other (please specify)

[Answer]: A. Basic only: add, subtract, multiply, divide

## Q2. [Product] User interaction style

How will someone use the calculator?

A. Importable Python module/library (functions called from code)
B. Command-line tool (arguments like `calc 2 + 3`)
C. Interactive REPL (type expressions, get results)
D. All of the above (module + CLI + REPL)
X. Other (please specify)

[Answer]: B. Command-line tool (arguments like `calc 2 + 3`)

## Q3. [Product] Number handling

How should the calculator handle numbers?

A. Integers only
B. Floating-point (decimals) only
C. Both integers and floats, preserving input type where possible
D. Decimal (exact) arithmetic to avoid floating-point rounding errors
X. Other (please specify)

[Answer]: A. Integers only

## Q4. [Product] Error handling

How should the calculator behave on invalid input or errors (e.g., division by zero)?

A. Raise a Python exception with a clear message
B. Return a special value (None, NaN, or an error string)
C. Print an error message and continue (for CLI/REPL)
D. A mix: exceptions for library use, friendly messages for CLI
X. Other (please specify)

[Answer]: B. Return a special value (None, NaN, or an error string)
