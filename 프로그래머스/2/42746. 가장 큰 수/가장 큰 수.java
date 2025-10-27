import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] snum = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            snum[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(snum, (o1, o2) -> (o2 + o1).compareTo(o1 + o2));
        
        if (snum[0].equals("0")) return "0";
        
        StringBuilder sb = new StringBuilder();
        for (String s: snum) {
            sb.append(s);
        }
        return sb.toString();
    }
}