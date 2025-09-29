import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        StringBuilder answer = new StringBuilder();
        char[] xc = X.toCharArray();
        char[] yc = Y.toCharArray();
        Arrays.sort(xc);
        Arrays.sort(yc);
        
        int lxc = xc.length - 1;
        int lyc = yc.length - 1;
        
        while(lxc >= 0 && lyc >= 0) {
            if (xc[lxc] == yc[lyc]) {
                answer.append(xc[lxc]);
                lxc--;
                lyc--;
            } else if (xc[lxc] > yc[lyc]){
                lxc--;
            } else {
                lyc--;
            }
        }
        
        if (answer.length() == 0) {
            return "-1";
        }
        
        if (answer.toString().matches("0+")) {
            return "0";
        }
        
        return answer.toString();
    }
}