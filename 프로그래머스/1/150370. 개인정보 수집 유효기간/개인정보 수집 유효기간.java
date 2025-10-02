import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList<>();
        int todaydate = convertDate(today);
        
        Map<String, Integer> m = new HashMap<>();
        for (String t: terms) {
            String[] split = t.split(" ");
            String type = split[0];
            int month = Integer.parseInt(split[1]);
            m.put(type, month);
        }
        
        for(int i = 0; i < privacies.length; i++) {
            String[] split = privacies[i].split(" ");
            String date = split[0];
            String type = split[1];
            int coldate = convertDate(date);
            int termM = m.get(type);
            int exp = coldate + (termM * 28) - 1;
            if (exp < todaydate) {
                answer.add(i + 1);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
    private int convertDate(String s) {
        String[] date = s.split("\\.");
        int y = Integer.parseInt(date[0]);
        int m = Integer.parseInt(date[1]);
        int d = Integer.parseInt(date[2]);
        return (y * 12 * 28) + (m * 28) + d;
    }
}