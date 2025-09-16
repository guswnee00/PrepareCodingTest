class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length - 1];
        
        if (arr.length < 2) {
            answer = new int[]{-1};
        }
        
        int min = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        
        int idx = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != min) {
                answer[idx++] = arr[i];
            }
        }
        return answer;
    }
}