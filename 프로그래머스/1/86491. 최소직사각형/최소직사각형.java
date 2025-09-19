class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxH = 0;
        int maxW = 0;
        for (int[] size: sizes) {
            int h = Math.max(size[0], size[1]);
            int w = Math.min(size[0], size[1]);
            
            if (h > maxH) maxH = h;
            if (w > maxW) maxW = w;
        }
        answer = maxH * maxW;
        return answer;
    }
}