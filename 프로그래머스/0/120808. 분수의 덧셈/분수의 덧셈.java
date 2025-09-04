class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        int numer = numer1*denom2 + numer2*denom1;
        int denom = denom1 * denom2;
        for (int i = Math.max(numer, denom);i > 0; i--) {
            // 최대공약수 찾아서 기약분수로 만들기
            if (numer%i == 0 && denom%i == 0){
                answer[0] = numer / i;
                answer[1] = denom / i;
                break;
            }
        }
        return answer;
    }
}