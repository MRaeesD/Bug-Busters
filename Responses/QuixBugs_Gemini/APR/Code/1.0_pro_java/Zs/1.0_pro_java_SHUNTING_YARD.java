// Added an else clause to handle the case when the operator has a higher precedence than the top of the stack.
} else {
                String operator = (String) token;
                while (!opstack.isEmpty() && precedence.get(operator) <= precedence.get(opstack.getLast())) {
                    rpntokens.add(opstack.pop());
                }
                opstack.push(operator);
            }
