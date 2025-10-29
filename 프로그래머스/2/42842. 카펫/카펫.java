class Solution {
    public int[] solution(int brown, int yellow) {
        int carpet = brown + yellow;
        
        for (int h = 3; h <= Math.sqrt(carpet); h++) {
            if (carpet % h == 0) {
                int w = carpet / h;
                
                if ((h - 2) * (w - 2) == yellow) {
                    return new int[]{w, h};
                }
            }
        }
        return new int[0];
    }
}