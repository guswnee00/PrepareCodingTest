import java.util.*;
class Solution {
    public long solution(long n) {
        char[] digit = Long.toString(n).toCharArray();
        Arrays.sort(digit);
        
        StringBuilder sb = new StringBuilder(new String(digit));
        sb.reverse();
        long answer = Long.parseLong(sb.toString());
        return answer;
    }
}