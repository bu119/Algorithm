class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int cnt = 0;
       	for (int number: numbers) {
            answer += number;
            cnt += 1;
        }
        answer /= cnt;
        return answer;
    }
}