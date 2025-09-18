class Solution {
    public String solution(String s) {
        String answer = "";
        int cnt = 0;
        String[] slist = s.split("");
        for (String word: slist) {
            if (word.contains(" ")) {
                cnt = 0;
            } else {
                cnt++;
            }
            
            if (cnt % 2 == 0) {
                answer += word.toLowerCase();
            } else {
                answer += word.toUpperCase();
            }
        }
        return answer;
    }
}