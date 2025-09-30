class Solution {
    public int solution(String s) {
        int answer = 0;
        int cntx = 0;
        int cnto = 0;
        char x = s.charAt(0);
        
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (cur == x) {
                cntx++;
            } else {
                cnto++;
            }
            
            if(cntx == cnto) {
                answer++;
                if (i + 1 < s.length()) {
                    x = s.charAt(i+1);
                }
                cntx = 0;
                cnto = 0;
            }
        }
        if (cntx != 0 || cnto != 0) {
            answer++;
        }
        return answer;
    }
}