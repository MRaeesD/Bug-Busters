if (token.equals("/") && b == 0.0) {
                    throw new ArithmeticException();
                } else {
                    BinaryOperator<Double> bin_op = op.get(token);
                    c = bin_op.apply(a, b);
                }
                stack.push(c); // The change is here
