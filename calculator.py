"""Simple integer calculator with a command-line interface."""


def add(a, b):
    """Return the sum of two integers."""
    return a + b


def subtract(a, b):
    """Return the difference of two integers."""
    return a - b


def multiply(a, b):
    """Return the product of two integers."""
    return a * b


def divide(a, b):
    """Return integer division of a by b, or None when b is zero."""
    if b == 0:
        return None
    return a // b


_OPERATORS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(operand1, operator, operand2):
    """Compute operand1 operator operand2; return None on invalid input."""
    try:
        a = int(operand1)
        b = int(operand2)
    except (ValueError, TypeError):
        return None
    operation = _OPERATORS.get(operator)
    if operation is None:
        return None
    return operation(a, b)


def main(argv=None):
    """Command-line entry point. Returns an exit code."""
    import sys

    if argv is None:
        argv = sys.argv[1:]
    if len(argv) != 3:
        print("Usage: calculator <operand> <operator> <operand>", file=sys.stderr)
        return 1
    result = calculate(argv[0], argv[1], argv[2])
    if result is None:
        print("Error: invalid input or division by zero", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
