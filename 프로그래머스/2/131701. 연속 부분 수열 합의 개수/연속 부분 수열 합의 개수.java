import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int[] arr = new int[2 * elements.length];
        for(int i = 0; i < 2 * elements.length; i++) {
            arr[i] = elements[i % elements.length];
        }
        
        int[] prefix = new int[2 * elements.length + 1];
        for (int i = 1; i <= 2 * elements.length; i++) {
            prefix[i] = prefix[i-1] + arr[i - 1];
        }
        
        Set<Integer> sums = new HashSet<>();
        
        for(int i = 1; i <= elements.length; i++) {
            for (int j = 0; j < elements.length; j++) {
                int e = i + j;
                int sum = prefix[e] - prefix[j];
                sums.add(sum);
            }
        }
        
        return sums.size();
    }
}