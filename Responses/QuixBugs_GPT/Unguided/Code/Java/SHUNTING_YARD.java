package java_programs;
import java.util.*;

public class SHUNTING_YARD {
    public static List<Object> shunting_yard(ArrayList<Object> tokens) {
        Map<String, Integer> precedence = new HashMap<>();
        precedence.put("+", 1);
        precedence.put("-", 1);
        precedence.put("*", 2);
        precedence.put("/", 2);

        ArrayList<Object> rpntokens = new ArrayList<>();
        ArrayDeque<String> opstack = new ArrayDeque<>();

        for (Object token : tokens) {
            if (token instanceof Integer) {
                rpntokens.add((Integer) token);
            } else {
                String operator = (String) token;
                while (!opstack.isEmpty() && 
                       precedence.containsKey(opstack.getLast()) && 
                       precedence.get(operator) <= precedence.get(opstack.getLast())) {
                    rpntokens.add(opstack.pop());
                }
                opstack.push(operator); // Fix: Add the operator to the stack
            }
        }

        while (!opstack.isEmpty()) {
            rpntokens.add(opstack.pop());
        }

        return rpntokens;
    }
}