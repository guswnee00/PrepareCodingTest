import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] h1 = {1, 2, 3, 4, 5};
        int[] h2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] h3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] s = new int[3];
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == h1[i % h1.length]) s[0]++;
            if (answers[i] == h2[i % h2.length]) s[1]++;
            if (answers[i] == h3[i % h3.length]) s[2]++;
        }
        int max = Math.max(s[0], Math.max(s[1], s[2]));
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            if (s[i] == max) {
                list.add(i+1);
            }
        }
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer; 
    }
}