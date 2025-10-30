import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> set = new HashSet<>();
        set.add(words[0]);
        
        for (int i = 1; i < words.length; i++) {
            String pre = words[i-1];
            String cur = words[i];
            
            if(set.contains(cur) || pre.charAt(pre.length() - 1) != cur.charAt(0)) {
                int person = (i % n) + 1;
                int turn = (i / n) + 1;
                return new int[]{person, turn};
            }
            set.add(cur);
        }
        return new int[]{0, 0};
    }
}