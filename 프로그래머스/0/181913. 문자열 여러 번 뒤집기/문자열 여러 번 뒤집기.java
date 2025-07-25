class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = my_string;
        int n = my_string.length();
        for (int i = 0; i < queries.length; i++) {
            int s = queries[i][0];
            int e = queries[i][1];
    		String reversed = "";
            for (int j = e; s <= j; j--) {
                reversed += answer.charAt(j);
            }
    		answer = answer.substring(0, s) + reversed + answer.substring(e + 1);
        }
        return answer;
    }
}