import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }
        
        for (String name: callings) {
            int rank = map.get(name);
            String front = players[rank - 1];
            players[rank - 1] = name;
            players[rank] = front;
            map.put(name, rank - 1);
            map.put(front, rank);
        }
        return players;
    }
}