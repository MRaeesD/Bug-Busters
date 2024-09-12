else:
            while opstack and precedence[token] <= precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
            opstack.append(token)  # Missing code to append the current \
                                     # operator to the opstack

            # Rest of the code
