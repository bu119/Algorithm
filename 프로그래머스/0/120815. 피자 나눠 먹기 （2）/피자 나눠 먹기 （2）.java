class Solution {
    public int solution(int n) {
        // 6과 n의 최소공배수 / 6?
        // 6과 n의 최대공약수
        int gcd = 0;
        int min = Math.min(6, n);
        for (int i = min; i > 0; i--) {
            if (6 % i == 0 & n % i == 0) {
                gcd = i;
                break;
            }
        }
        // 최소공배수 / 6
        int answer = (n * 6 / gcd) / 6;        
        return answer;
    }
}