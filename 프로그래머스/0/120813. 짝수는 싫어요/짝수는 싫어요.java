class Solution {
    public int[] solution(int n) {
        int m = n / 2;
        if (n % 2 == 1) {
            m += 1;
        }
        int[] answer = new int[m];
        for (int i = 0; i < m; i++) {
            answer[i] = i*2+1;
        }
        return answer;
    }
}