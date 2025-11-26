class Solution {
    static boolean[] visited;
    static int answer;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        dfs(k, dungeons, 0);
        return answer;
    }
    
    private void dfs(int k, int[][] dungeons, int cnt) {
        answer = Math.max(answer, cnt);
        
        for(int i = 0; i < dungeons.length; i++) {
            int req = dungeons[i][0];
            int cons = dungeons[i][1];
            
            if(!visited[i] && k >= req) {
                visited[i] = true;
                dfs(k-cons, dungeons, cnt+1);
                visited[i] = false;
            }
        }
    }
}