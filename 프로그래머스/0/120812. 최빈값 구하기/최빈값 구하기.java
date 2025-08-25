import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int max = 0;
        int n = array.length;
        Arrays.sort(array);
        int cnt = 1;
        for (int i = 1; i < n+1; i++) {
        	if (i != n && array[i] == array[i-1]) {
            	cnt += 1;
            } else {
            	if (cnt > max) {
                	max = cnt;
                    answer = array[i-1];
                } else if (cnt == max) {
                	answer = -1;
                }
                cnt = 1;
            }
        }
        return answer;
    }
}