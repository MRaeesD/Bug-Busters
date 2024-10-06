java
public static int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b); // Pass 'b' as the first parameter instead of 'a % b'
    }
}
