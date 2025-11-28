import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<int[]> b = new LinkedList<>();
        int cw = 0;
        int idx = 0;
        
        while (idx < truck_weights.length || !b.isEmpty()) {
            answer++;
            
            if (!b.isEmpty() && b.peek()[1] == answer) {
                cw -= b.poll()[0];
            }
            
            if(idx < truck_weights.length) {
                int nt = truck_weights[idx];
                if (cw + nt <= weight && b.size() < bridge_length) {
                    cw += nt;
                    b.offer(new int[]{nt, answer + bridge_length});
                    idx++;
                }
            }
        }
        
        return answer;
    }
}