class Solution {
    public String[] solution(String[] names) {
        int n = names.length / 5;            
        if (names.length % 5 != 0) {
            n += 1;
        }
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            answer[i] = names[i*5];
        }
        return answer;
    }
}