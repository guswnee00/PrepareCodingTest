import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        Deque<String> cache = new ArrayDeque<>();
        int answer = 0;
        
        if (cacheSize == 0) return cities.length * 5;
        
        for(String c: cities) {
            c = c.toLowerCase();
            
            if (cache.remove(c)) {
                cache.addLast(c);
                answer += 1;
            } else {
                if (cache.size() == cacheSize) {
                    cache.removeFirst();
                }
                cache.addLast(c);
                answer += 5;
            }
        }
        return answer;
    }
}