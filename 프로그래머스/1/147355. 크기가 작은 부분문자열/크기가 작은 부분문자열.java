class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int n = p.length();
        for (int i = 0; i < t.length()-n+1; i++) {
            if (t.substring(i,i+n).compareTo(p) <= 0) {
                answer ++;
            }
        }
        return answer;
    }
}