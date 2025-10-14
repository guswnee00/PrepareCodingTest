class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean f = true;
        
        for (char c: s.toCharArray()) {
            if (c == ' ') {
                sb.append(c);
                f = true;
            } else {
                if (f) {
                    sb.append(Character.isLetter(c) ? Character.toUpperCase(c) : c);
                    f = false;
                } else {
                    sb.append(Character.toLowerCase(c));
                }
            }
        }
        return sb.toString();
    }
}