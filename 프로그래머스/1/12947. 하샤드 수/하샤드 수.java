class Solution {
    public boolean solution(int x) {
        if (x % sum(x) == 0) {
            return true;
        } else {
            return false;
        }
    }
    
    public int sum(int x) {
        String s = String.valueOf(x);
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            sum += Character.getNumericValue(s.charAt(i));
        }
        return sum;
    }
}