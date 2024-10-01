def rpn_eval(tokens):
    def op(symbol, a, b):
        if symbol == '/' and b == 0:
            raise ZeroDivisionError("division by zero")
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, (int, float)):  # Handle both integers and floats
            stack.append(token)
        elif token in ('+', '-', '*', '/'):  # Explicit operator check
            b = stack.pop()  # Correct order: b is popped first
            a = stack.pop()  # a is popped second
            stack.append(
                op(token, a, b)
            )
        else:
            raise ValueError(f"Invalid token: {token}")

    return stack.pop()