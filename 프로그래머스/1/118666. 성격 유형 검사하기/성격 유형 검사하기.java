import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        Map<Character, Integer> m = new HashMap<>();
        
        for (int i = 0; i < choices.length; i++) {
            int v = choices[i];
            if (v > 0 && v < 4) {
                char c = survey[i].charAt(0);
                m.put(c, m.getOrDefault(c, 0) + 4 - v);
            } else if (v > 4) {
                char c = survey[i].charAt(1);
                m.put(c, m.getOrDefault(c, 0) + v - 4);
            }
        }
        StringBuilder sb = new StringBuilder();
        char[][] types = { {'R','T'}, {'C','F'}, {'J','M'}, {'A','N'} };
        
        for(char[] type: types) {
            char f = type[0];
            char s = type[1];
            int fs = m.getOrDefault(f, 0);
            int ss = m.getOrDefault(s, 0);
            
            if (fs >= ss) {
                sb.append(f);
            } else {
                sb.append(s);
            }
        }
        return sb.toString();
    }
}