package java_programs;

import java.util.*;

public class SHUNTING_YARD {
    public static List<Object> shunting_yard(ArrayList<Object> tokens) {
        Map<String, Integer> precedence = new HashMap<String, Integer>();
        precedence.put("+", 1);
        precedence.put("-", 1);
        precedence.put("*", 2);
        precedence.put("/", 2);

        ArrayList<Object> rpntokens = new ArrayList<>(100);
        ArrayDeque<String> opstack = new ArrayDeque<>();

        for (Object token : tokens) {
            if (token instanceof Integer) {
                rpntokens.add(token);
            } else {
                String operator = (String) token;
                if (operator.equals("(")) {
                    opstack.push(operator);
                } else if (operator.equals(")")) {
                    while (!opstack.isEmpty() && !opstack.getLast().equals("(")) {
                        rpntokens.add(opstack.pop());
                    }
                    opstack.pop(); // Pop the '(' from the stack
                } else {
                    while (!opstack.isEmpty() && precedence.get(operator) <= precedence.get(opstack.getLast())) {
                        rpntokens.add(opstack.pop());
                    }
                    opstack.push(operator); // Push the current operator onto the stack
                }
            }
        }

        while (!opstack.isEmpty()) {
            rpntokens.add(opstack.pop());
        }

        return rpntokens;
    }
}