class Solution {
    public long solution(int price, int money, int count) {
        long cost = (long) count * price * (1 + count) / 2;
        long answer = 0;
        if (money < cost) {
            answer = cost - money;
        }
        return answer;
    }
}