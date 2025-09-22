class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] numWords = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < numWords.length; i++) {
            s = s.replaceAll(numWords[i], String.valueOf(i));
        }
        answer = Integer.parseInt(s);
        return answer;
    }
}