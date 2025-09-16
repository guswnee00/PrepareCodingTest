class Solution {
    public int solution(String s) {
        int answer = 0;
        int idx = 0;
        char sign = s.charAt(0);
        
        if (sign == '-' || sign == '+') {
            idx = 1;
        }
        
        answer = Integer.parseInt(s.substring(idx));
        
        if (sign == '-') {
            answer *= -1;
        }
        
        return answer;
    }
}