class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            int com = arr1[i] | arr2[i];
            String bi = Integer.toBinaryString(com);
            bi = String.format("%" + n + "s", bi).replace(' ', '0');
            bi = bi.replace('1', '#').replace('0', ' ');
            answer[i] = bi;
        }
        return answer;
    }
}