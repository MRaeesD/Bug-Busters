import java.util.*;

public class Main {
    public static void main(String[] args) {

        IOHandler io = new IOHandler();
        int n = io.nextInt();
        int[][] a = io.nextIntArray(n, n);
        int[][] b = io.nextIntArray(n, n);
        io.close();

        if (isMatchAnswer(a, b)) {
            io.output("Yes");
            return;
        }

        for (int i = 0; i < 3; i++) {
            if (isMatchAnswer(a, b)) { //bug
                io.output("Yes");
                return;
            }

            a = rotate(a);
        }
        io.output("No");
    }

    private static boolean isMatchAnswer(int[][] a, int[][] b) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                if (a[i][j] == 1 && b[i][j] != 1) return false;
            }
        }
        return true;
    }

    private static int[][] rotate(int[][] source) {
        int n = source.length;
        int[][] result = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[n-1-j][i] = source[i][j];
            }
        }

        return result;
    }

    private static class IOHandler {
        private Scanner sc = new Scanner(System.in);
        private void close() {this.sc.close();}
        private int nextInt() {return this.sc.nextInt();}
        private int[] nextIntArray(int size) {
            int[] array = new int[size];
            for (int i = 0; i < size; i++) array[i] = this.sc.nextInt();
            return array;
        }
        private int[][] nextIntArray(int size1, int size2) {
           int[][] array = new int[size1][size2];
           for (int i = 0; i < size1; i++) array[i] = nextIntArray(size2);
           return array;
        }
        private <T> void output(T result) {System.out.println(result);}
    }
}

