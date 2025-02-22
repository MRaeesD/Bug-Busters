import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        pro1();
    }

    private static void pro1(){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int D = scanner.nextInt();
        int[] T = new int[N];

        for(int i = 0; i < N; i++){
            T[i] = scanner.nextInt();
        }
        scanner.close();

        for(int i = 1; i < N; i++){
            if(T[i]-T[i-1] <= D) //bug
                System.out.println(T[i]);
                return;
        }
        System.out.println(-1);
    }

    private static void arr2(){
        ArrayList<ArrayList<Integer>> temp = new ArrayList<ArrayList<Integer>>();
        for (int i=0; i< 10; i++){
            temp.add(new ArrayList<Integer>());
            for (int j=0; j< 10; j++){
                temp.get(i).add(j);
                System.out.println(temp.get(i).get(j));
            }
        }
    }

    private static void Bfs(){
        Scanner scanner = new Scanner(System.in);
        int N, M;
        N = scanner.nextInt();
        M = scanner.nextInt();

        ArrayList<Integer>[] G = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            G[i] = new ArrayList<Integer>();
        }

        for(int i = 0; i < M; i++){
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            G[a].add(b);
            G[b].add(a);
        }
        scanner.close();

        int[] dist = new int[N];
        java.util.Arrays.fill(dist, -1);

        ArrayList<Integer>[] nodes = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            nodes[i] = new ArrayList<Integer>();
        }

        dist[0] = 0;
        nodes[0].add(0);

        for (int i = 0; i < N; i++){
            for(int node: nodes[i]){
                for (int g: G[node]){

                    if (dist[g] != -1)
                        continue;
                    
                    dist[g] = i + 1;
                    nodes[i + 1].add(g);
                }
            }
        }

        for (int d: dist){
            System.out.println(d);
        }
    }

    public static void Click(){
        Scanner scanner = new Scanner(System.in);
        int N, D;
        N = scanner.nextInt();
        D = scanner.nextInt();

        int[] T = new int[N];
        
        for(int i = 0; i < N; i++)
            T[i] = scanner.nextInt();
        scanner.close();

        for(int i = 1; i < N; i++){
            if(Math.abs(T[i] - T[i-1]) <= D){
                System.out.println(T[i]);
                System.exit(0);
            }
        }

        System.out.println(-1);
        System.exit(0);
    }
}

