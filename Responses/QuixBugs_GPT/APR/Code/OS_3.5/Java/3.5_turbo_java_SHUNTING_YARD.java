java
} else {
    String operator = (String) token;
    while (!opstack.isEmpty() && precedence.get(operator) <= precedence.get(opstack.getLast())) {
        rpntokens.add(opstack.pop());
    }
}
