def shunting_yard(tokens):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(token)
        elif token in precedence:
            while opstack and precedence[opstack[-1]] >= precedence[token]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
        else:
            raise ValueError(f"Unexpected token {token}")

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens