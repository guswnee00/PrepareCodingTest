class Solution {
    public int[] solution(String s) {
        int bicnt = 0;
        int zcnt = 0;
        
        while(!s.equals("1")) {
            int zero = s.length() - s.replace("0", "").length();
            zcnt += zero;
            
            s = s.replace("0", "");
            int len = s.length();
            
            s = Integer.toBinaryString(len);
            bicnt++;
        }
        return new int[]{bicnt, zcnt};
    }
}