class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = my_string;
        int n = my_string.length();
        for (int i = 0; i < queries.length; i++) {
            int s = queries[i][0];
            int e = queries[i][1];
    		String reversed = new StringBuilder(answer.substring(s, e + 1)).reverse().toString();
    		answer = answer.substring(0, s) + reversed + answer.substring(e + 1);
        }
        return answer;
    }
}