while (n != 0) {
    n = (n & (n - 1));  // Change made here
    count++;
}
