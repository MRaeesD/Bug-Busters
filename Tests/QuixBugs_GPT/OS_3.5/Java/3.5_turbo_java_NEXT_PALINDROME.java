java
otherwise.addAll(Collections.nCopies(digit_list.length, 0));
 

Changed to:

java
otherwise.addAll(Arrays.asList(Arrays.stream(digit_list).boxed().toArray(Integer[]::new)));
