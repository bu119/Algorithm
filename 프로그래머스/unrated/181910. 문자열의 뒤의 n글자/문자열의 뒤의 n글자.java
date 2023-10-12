class Solution {
    public String solution(String my_string, int n) {
        int m = my_string.length();
        String answer = my_string.substring(m-n);
        return answer;
    }
}