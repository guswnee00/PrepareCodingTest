class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right; i++) {
            if (isSqrt(i)) {
                answer -= i;
            } else {
                answer += i;
            }
        }
        return answer;
    }
    
    private boolean isSqrt(int n) {
        int i = (int)Math.sqrt(n);
        return i*i == n;
    }
}