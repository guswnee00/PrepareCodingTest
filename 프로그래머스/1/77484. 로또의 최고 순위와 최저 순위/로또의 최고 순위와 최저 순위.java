import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int zcnt = 0;
        int mcnt = 0;
        
        Set<Integer> set = new HashSet<>();
        for (int n: win_nums) {
            set.add(n);
        }
        
        for (int n: lottos) {
            if (n == 0) {
                zcnt++;
            } else if (set.contains(n)) {
                mcnt++;
            }
        }
        int maxcnt = mcnt + zcnt;
        return new int[] {getRank(maxcnt), getRank(mcnt)};
    }
    
    private int getRank(int n) {
        switch (n) {
            case 6: return 1;
            case 5: return 2;
            case 4: return 3;
            case 3: return 4;
            case 2: return 5;
            default: return 6;
        }
    }
}