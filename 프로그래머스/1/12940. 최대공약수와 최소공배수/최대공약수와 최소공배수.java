class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        int min = Math.min(n,m);
        // 최대공약수 찾기
        for (int i = min; i > 0; i--) {
            if (n % i == 0 & m % i == 0) {
                answer[0] = i;
                break;
            }
        }
        // 최소공배수 찾기
        answer[1] = n * m / answer[0];
        
        return answer;
    }
}