class Solution {
    public String solution(String s) {
        String answer = "";
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == ' '){
                answer += " ";
                
            } else if (i == 0 || s.charAt(i - 1) == ' ') {
                answer += Character.toUpperCase(s.charAt(i));
                
            } else {
                answer += Character.toLowerCase(s.charAt(i));
            }
        }
             
        return answer;
    }
}