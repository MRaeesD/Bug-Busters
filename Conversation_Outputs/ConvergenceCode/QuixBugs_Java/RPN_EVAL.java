package java_programs;
import java.util.*;
import java.util.function.BinaryOperator;

public class RPN_EVAL {
    public static Double rpn_eval(ArrayList tokens) {
        Map<String, BinaryOperator<Double>> op = new HashMap<String, BinaryOperator<Double>>();
        op.put("+", (a, b) -> a + b);
        op.put("-", (a, b) -> a - b);
        op.put("*", (a, b) -> a * b);
        op.put("/", (a, b) -> {
            if (b == 0) {
                throw new ArithmeticException("Division by zero");
            }
            return a / b;
        });

        // Use generics for type safety
        Stack<Double> stack = new Stack<>();

        for (Object token : tokens) {
            if (token instanceof Double) {
                stack.push((Double) token);
            } else {
                String operator = (String) token;
                Double b = stack.pop(); // Correct order: pop b first
                Double a = stack.pop();
                BinaryOperator<Double> bin_op = op.get(operator);
                Double c = bin_op.apply(a, b); // Apply the operation
                stack.push(c);
            }
        }

        return stack.pop();
    }
}