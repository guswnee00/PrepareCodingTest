import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        List<Character> alp = new ArrayList<>();
        for(char c = 'a'; c <= 'z'; c++) {
            if(skip.indexOf(c) == -1) {
                alp.add(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char c: s.toCharArray()) {
            int now = alp.indexOf(c);
            int idx = (now + index) % alp.size();
            sb.append(alp.get(idx));
        }
        return sb.toString();
    }
}