java
for (Integer count : counts) { // Fixed iteration over counts instead of arr
    sorted_arr.addAll(Collections.nCopies(count, i));
    i++;
}
