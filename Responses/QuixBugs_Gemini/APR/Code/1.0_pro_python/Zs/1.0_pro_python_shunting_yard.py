...
        else:
            while opstack and precedence[token] <= precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
            # Here the token is pushed to the `opstack` when it is an operator
            opstack.append(token)
...
