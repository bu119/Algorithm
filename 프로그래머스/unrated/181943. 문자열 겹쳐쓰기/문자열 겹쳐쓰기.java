class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        
        int n = my_string.length();
        int m = overwrite_string.length();
        
        for (int i=0; i<n; i++) {
            if (i<s) {
                answer += my_string.charAt(i);
            } else if (i-s < m) {
                answer += overwrite_string.charAt(i-s);
            } else {
                answer += my_string.charAt(i);
            }
        }
        
        return answer;
    }
}