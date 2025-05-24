class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int n = myString.length();
        int m = pat.length();
        
        for (int i = 0; i < n - m + 1; i++) {
            if (myString.substring(i, i+m).toLowerCase().equals(pat.toLowerCase())) {
                answer = 1;
                break;
            }
        }
        
        return answer;
    }
}