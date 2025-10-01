import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        Stack<Integer> s = new Stack<>();
        int h = 0;
        for (int i = 0; i < ingredient.length; i++) {
            s.push(ingredient[i]);
            if (s.size() >= 4) {
                h = s.size();
                if (s.get(h - 1) == 1 && s.get(h - 2) == 3 && s.get(h - 3) == 2 && s.get(h - 4) == 1 ) {
                    answer++;
                    s.pop(); 
                    s.pop(); 
                    s.pop(); 
                    s.pop();
                }
            }
        }
        return answer;
    }
}