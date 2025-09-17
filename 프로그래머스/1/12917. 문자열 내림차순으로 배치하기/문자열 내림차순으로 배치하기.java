import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        char[] clist = s.toCharArray();
        Arrays.sort(clist);
        StringBuilder sb = new StringBuilder(new String(clist));
        sb.reverse();
        answer = sb.toString();
        return answer;
    }
}