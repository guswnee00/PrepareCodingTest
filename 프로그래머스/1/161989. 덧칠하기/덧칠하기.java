class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int roller = 0;
        for (int s: section) {
            if (s > roller) {
                answer++;
                roller = s + m - 1;
            }
        }
        return answer;
    }
}