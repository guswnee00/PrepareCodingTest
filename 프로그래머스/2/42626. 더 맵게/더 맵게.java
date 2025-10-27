import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int sco: scoville) {
            pq.offer(sco);
        }
        
        int mix = 0;
        
        while(pq.size() > 1 && pq.peek() < K) {
            int f = pq.poll();
            int s = pq.poll();
            int newSco = f + (s * 2);
            pq.offer(newSco);
            mix++;
        }
        
        return pq.peek() >= K ? mix: -1;
    }
}