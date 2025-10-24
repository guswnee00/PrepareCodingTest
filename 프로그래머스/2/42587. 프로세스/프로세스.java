import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new LinkedList<>();
        PriorityQueue<Integer> pq = new PriorityQueue(Collections.reverseOrder());
        
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[]{priorities[i], i});
            pq.add(priorities[i]);
        }
        
        int o = 0;
        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            
            if (now[0] == pq.peek()) {
                pq.poll();
                o++;
                
                if(now[1] == location) {
                    return o;
                }
            } else {
                queue.add(now);
            }
        }
        return -1;
    }
}