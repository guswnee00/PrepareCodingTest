class Solution {
    public String solution(String s) {
        String[] list = s.split(" ");
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for(String num : list) {
            int cur = Integer.parseInt(num);
            if (cur < min) min = cur;
            if (cur > max) max = cur;
        }
        
        return min + " " + max;
    }
}