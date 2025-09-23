class Solution {
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < food.length; i++) {
            int cnt = food[i] / 2;
            for (int j = 0; j < cnt; j++) {
                sb.append(i);
            }
        }
        
        StringBuilder answer = new StringBuilder();
        answer.append(sb);
        answer.append(0);
        answer.append(sb.reverse());
        return answer.toString();
    }
}