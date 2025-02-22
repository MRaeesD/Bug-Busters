import java.util.*;
import java.io.*;
class Main {
  public static void main(String[] arg) {
    FastScanner sc = new FastScanner();
    int n = Integer.parseInt(sc.next());
    int a[][] = new int[n][n];
    int b[][] = new int[n][n];
    int ans0 = 0;
    int ans90 = 0;
    int ans180 = 0;
    int ans270 = 0;
    int all = 0;
    String despAns = "No";
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        a[i][j] = Integer.parseInt(sc.next());
        if(a[i][j] == 1) all++;
      }
    }
    for(int k = 0; k < n; k++) {
      for(int l = 0; l < n; l++) {
        b[k][l] = Integer.parseInt(sc.next());
      }
    }
    for(int row = 0; row < n; row++) {
      for(int col = 0; col < n; col++) {
        if(a[row][col] == 0) continue;
        if(a[row][col] == b[row][col]) ans0++;
        if(a[row][col] == b[n - col - 1][row]) ans90++;
        if(a[row][col] == b[n - row - 1][n - col - 1]) ans180++;
        if(a[row][col] == b[col][n - row - 1]) ans0++;        //bug
      }
    }
    if(ans0 == all || ans90 == all || ans180 == all || ans270 == all) despAns = "Yes";
    System.out.println(despAns);
  }
}


class FastScanner {
  private final InputStream in = System.in;
  private final byte[] buffer = new byte[1024];
  private int ptr = 0;
  private int buflen = 0;
  private boolean hasNextByte() {
    if (ptr < buflen) {
      return true;
    }else{
      ptr = 0;
      try {
        buflen = in.read(buffer);
      } catch (IOException e) {
        e.printStackTrace();
      }
      if (buflen <= 0) {
        return false;
      }
    }
    return true;
  }
  private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
  private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
  private void skipUnprintable() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;}
  public boolean hasNext() { skipUnprintable(); return hasNextByte();}
  public String next() {
    if (!hasNext()) throw new NoSuchElementException();
    StringBuilder sb = new StringBuilder();
    int b = readByte();
    while(isPrintableChar(b)) {
      sb.appendCodePoint(b);
      b = readByte();
    }
    return sb.toString();
  }
  public long nextLong() {
    if (!hasNext()) throw new NoSuchElementException();
    long n = 0;
    boolean minus = false;
    int b = readByte();
    if (b == '-') {
      minus = true;
      b = readByte();
    }
    if (b < '0' || '9' < b) {
      throw new NumberFormatException();
    }
    while(true){
      if ('0' <= b && b <= '9') {
        n *= 10;
        n += b - '0';
      }else if(b == -1 || !isPrintableChar(b)){
        return minus ? -n : n;
      }else{
        throw new NumberFormatException();
      }
      b = readByte();
    }
  }
}

