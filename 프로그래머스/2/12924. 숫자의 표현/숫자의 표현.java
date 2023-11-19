class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            int ssum = 0;
            for (int j = i; j <= n; j++) {
                ssum += j;
                if (ssum == n){
                    answer += 1;
                    break;
                } else if (ssum > n){
                    break;
                }
            }
        }
        return answer;
    }
}