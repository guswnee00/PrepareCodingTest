class Solution {
    public String solution(int a, int b) {
        int[] days = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] week = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int idx = 5;
        int day = b - 1;
        for (int i = 0; i < a-1; i++) {
            day += days[i];
        }
        int idx2 = (idx + day) % 7;
        return week[idx2];
    }
}