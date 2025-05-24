class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int n = num_list.length;
            
        if (n >= 11) {
            for (int i = 0; i < n; i++) {
                answer += num_list[i];
            }
        } else {
            answer = 1;
            for (int i = 0; i < n; i++) {
                answer *= num_list[i];
            }
        }
        return answer;
    }
}