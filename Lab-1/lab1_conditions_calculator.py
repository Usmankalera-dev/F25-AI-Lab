"""Lab 1: conditional statements and a safe dynamic calculator."""

import ast
import operator


# Only arithmetic operators are permitted in calculator expressions.
_ALLOWED_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}
_ALLOWED_UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def evaluate_expression(expression: str) -> float:
    """Evaluate a numeric arithmetic expression without using eval()."""
    tree = ast.parse(expression, mode="eval")

    def evaluate(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BINARY_OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return _ALLOWED_BINARY_OPERATORS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARY_OPERATORS:
            return _ALLOWED_UNARY_OPERATORS[type(node.op)](evaluate(node.operand))
        raise ValueError("Use only numbers, parentheses, and + - * / % ** operators.")

    return evaluate(tree)


def classify_integer(x: int) -> str:
    """Return the required message for the integer classification task."""
    if x < 0:
        return "Negative changed to zero"
    if x == 0:
        return "Zero"
    if x == 1:
        return "Single"
    return "More"


def main() -> None:
    try:
        x = int(input("Please enter an integer: "))
        print(classify_integer(x))
    except ValueError:
        print("Error: please enter a valid integer.")

    print("\nDynamic calculator (blank expression to quit)")
    while True:
        expression = input("Expression: ").strip()
        if not expression:
            break
        try:
            print(f"Result: {evaluate_expression(expression)}")
        except (SyntaxError, ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
