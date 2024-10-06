java
public static ArrayList<Integer> sieve(Integer max) {
    ArrayList<Integer> primes = new ArrayList<Integer>();
    primes.add(2); // Adding 2 as the first prime number
    for (int n=3; n<max+1; n++) {
        if (any(list_comp(n, primes.subList(1, primes.size())))) {
            primes.add(n);
        }
    }
    return primes;
}
