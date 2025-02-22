import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

  static BufferedReader br;

  public static void main(String[] args) {
    br = new BufferedReader(new InputStreamReader(System.in));
    try {
      br = new BufferedReader(new FileReader("input.txt"));
    } catch (Exception e) {}

    int N = readInt();
    int Q = readInt();
    int[][] query = readMultiIntArray(Q);
    ArrayList<ArrayList<Integer>> box = new ArrayList<>(N + 1);
    ArrayList<HashSet<Integer>> card = new ArrayList<>(200001);
    for (int i = 0; i < N + 1; i++) {
      box.add(new ArrayList<>());
    }
    for (int i = 0; i < 200001; i++) {
      card.add(new HashSet<>());
    }
    for (int[] i : query) {
      if (i[0] == 1) {
        box.get(i[2]).add(i[1]);
        card.get(i[1]).add(i[2]);
      }
      if (i[0] == 2) {
        Collections.sort(box.get(i[1]), null);
        System.out.println(
          box
            .get(i[1])
            .stream()
            .map(Object::toString)
            .collect(Collectors.joining(" "))
        );
      }
      if (i[0] == 3) {
        List<Integer> list = new ArrayList<>(card.get(i[1]));
        Collections.sort(list);
        System.out.println(
          card //bug
            .get(i[1])
            .stream()
            .map(Object::toString)
            .collect(Collectors.joining(" "))
        );
      }
    }

    try {
      br.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public static int[][] rotate90(int[][] matrix) {
    
    int n = matrix.length;
    int[][] rotated = new int[n][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        rotated[j][n - i - 1] = matrix[i][j];
      }
    }
    return rotated;
  }

  public static boolean check(int[][] A, int[][] B) {
    
    int n = A[0].length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (A[i][j] == 1) {
          if (B[i][j] == 0) {
            return false;
          }
        }
      }
    }
    return true;
  }

  public static int[] readIntArray() {
    
    int[] array = null;
    try {
      array =
        Arrays
          .stream(br.readLine().split(" "))
          .mapToInt(Integer::parseInt)
          .toArray();
    } catch (IOException ex) {}
    return array;
  }

  public static int[][] readMultiIntArray(int num) {
    
    int[][] array = new int[num][];
    for (int i = 0; i < num; i++) {
      array[i] = readIntArray();
    }
    return array;
  }

  public static String[] readStringArray() {
    
    String[] array = null;
    try {
      array = br.readLine().split(" ");
    } catch (IOException ex) {}
    return array;
  }

  public static int readInt() {
    
    int num = 0;
    try {
      num = Integer.parseInt(br.readLine());
    } catch (IOException ex) {}
    return num;
  }

  public static String readString() {
    
    String str = null;
    try {
      str = br.readLine();
    } catch (IOException ex) {}
    return str;
  }
}

