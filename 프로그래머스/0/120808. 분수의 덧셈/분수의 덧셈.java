class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        int numer = numer1*denom2 + numer2*denom1;
        int denom = denom1 * denom2;
        int gcd = 1;
        for (int i = Math.max(numer, denom);i > 1; i--) {
            if (numer%i == 0 && denom%i == 0){
                // 최대공약수
                gcd = i;
                break;
            }
        }
        answer[0] = numer / gcd;
        answer[1] = denom / gcd;
        return answer;
    }
}