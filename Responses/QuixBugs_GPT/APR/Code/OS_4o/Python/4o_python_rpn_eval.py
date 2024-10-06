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
        if isinstance(token, float):
            stack.append(token)
        else:
            b = stack.pop()  # Changed the order of popping
            a = stack.pop()  # Changed the order of popping
            stack.append(
                op(token, a, b)  # Adjusted so operands are passed correctly
            )

    return stack.pop()
