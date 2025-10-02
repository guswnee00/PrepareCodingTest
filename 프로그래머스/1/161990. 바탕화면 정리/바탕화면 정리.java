class Solution {
    public int[] solution(String[] wallpaper) {
        int t = Integer.MAX_VALUE;
        int l = Integer.MAX_VALUE;
        int b = Integer.MIN_VALUE;
        int r = Integer.MIN_VALUE;
        
        for (int i = 0; i < wallpaper.length; i++) {
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    t = Math.min(i, t);
                    l = Math.min(j, l);
                    b = Math.max(i+1, b);
                    r = Math.max(j+1, r);
                }
            }
        }
        return new int[]{t, l, b, r};
    }
}