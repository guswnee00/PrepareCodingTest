import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        List<Integer> l = new ArrayList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            int rday = (int) Math.ceil((double) remain/speeds[i]);
            
            if(q.isEmpty()) {
                q.offer(rday);
                continue;
            }
            
            if(q.peek() < rday) {
                l.add(q.size());
                q.clear();
            }
            
            q.offer(rday);
        }
        
        l.add(q.size());
        
        return l.stream().mapToInt(Integer::intValue).toArray();
    }
}