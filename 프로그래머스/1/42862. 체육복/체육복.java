import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> ls = new HashSet<>();
        Set<Integer> rs = new HashSet<>();
        
        for (int l: lost) ls.add(l);
        for (int r: reserve) {
            if (ls.contains(r)) {
                ls.remove(r);
            } else {
                rs.add(r);
            }    
        }
        for (int l : new HashSet<>(ls)) {
            if (rs.contains(l - 1)) {
                rs.remove(l - 1);
                ls.remove(l);
            } else if (rs.contains(l + 1)) {
                rs.remove(l + 1);
                ls.remove(l);
            }
        }
        return n - ls.size();
    }
}