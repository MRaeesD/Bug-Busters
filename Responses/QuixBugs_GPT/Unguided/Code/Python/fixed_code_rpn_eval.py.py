def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, (float, int)):  # Fix to accept both float and int
            stack.append(token)
        else:
            b = stack.pop()  # Fix order: pop second operand first
            a = stack.pop()  # pop first operand
            stack.append(
                op(token, a, b)
            )

    return stack.pop()