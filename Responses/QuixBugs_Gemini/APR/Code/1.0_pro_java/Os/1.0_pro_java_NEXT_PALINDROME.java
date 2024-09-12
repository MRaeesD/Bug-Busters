ArrayList<Integer> otherwise = new ArrayList<Integer>();
        otherwise.add(1);
        otherwise.addAll(Collections.nCopies(digit_list.length - 1, 0)); // change made here
        otherwise.add(1);

        return String.valueOf(otherwise);
