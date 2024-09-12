def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: b - a,  # Corrected order of operands for subtraction
            '*': lambda a, b: a * b,
            '/': lambda a, b: b / a   # Corrected order of operands for division
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(
                op(token, a, b)
            )

    return stack.pop()
