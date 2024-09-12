String result = "";
        String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int i;
        while (num > 0) {
            i = num % b;
            num = num / b; 
            result = String.valueOf(alphabet.charAt(i)) + result; // reversed the string here 
        }

        return result;
