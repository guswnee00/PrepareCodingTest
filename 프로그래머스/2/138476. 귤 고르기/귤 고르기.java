import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int size : tangerine) {
            map.put(size, map.getOrDefault(size, 0) + 1);
        }
        
        List<Integer> list = new ArrayList<>(map.values());
        list.sort(Collections.reverseOrder());
        
        int answer = 0;
        int remain = k;
        
        for (int l: list) {
            remain -= l;
            answer++;
            
            if (remain <= 0) break;
        }
        return answer;
    }
}