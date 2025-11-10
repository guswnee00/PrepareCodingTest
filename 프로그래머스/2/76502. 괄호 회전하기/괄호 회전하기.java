import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        for(int i = 0; i < s.length(); i++) {
            Stack<Character> stack = new Stack<>();
            String rotated = s.substring(i) + s.substring(0,i);
            boolean isV = true;

            for (char c: rotated.toCharArray()) {
                if(c == '(' || c == '{' || c == '[') {
                    stack.push(c);
                } else {
                    if (stack.isEmpty()) {
                        isV = false;
                        break;
                    }
                    char t = stack.pop();
                    if (!((t == '(' && c == ')') || (t == '[' && c == ']') || (t == '{' && c == '}'))) {
                        isV = false;
                        break;
                    }
                }
            }
            if (isV && stack.isEmpty()) answer++;
        }
        return answer;
    }
}