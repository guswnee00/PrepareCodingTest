import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new LinkedList<>();
        
        q.offer(new int[] {0, 0, 1});
        visited[0][0] = true;
        
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            int d = cur[2];
            
            if (x == n-1 && y == m-1) {
                return d;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.offer(new int[] {nx, ny, d+1});
                }
            }
        }
        return -1;
    }
}