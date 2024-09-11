import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static int N;
    static int[] parents;
    static boolean[] visited;
    static ArrayList<Integer>[] list;


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        N = scanner.nextInt();
        parents = new int[N + 1];   // 각 노드의 부모 노드 저장
        visited = new boolean[N + 1];   // 방문 확인 배열
        list = new ArrayList[N + 1];   // 노드별로 연결된 노드들을 저장할 배열

        for (int i = 1; i <= N; i++) {
            list[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < N - 1; i++) {
            int v1 = scanner.nextInt();
            int v2 = scanner.nextInt();
            list[v1].add(v2);
            list[v2].add(v1);
        }

        dfs(1);

        for (int i = 2; i <= N; i++) {
            System.out.println(parents[i]);
        }

    }

    static public void dfs(int v) {
        visited[v] = true;

        for (int vertex : list[v]) {
            if (!visited[vertex]) {
                parents[vertex] = v;
                dfs(vertex);
            }
        }
    }

}