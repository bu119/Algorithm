class Solution {
    public long solution(int price, int money, int count) {
        long cost = (long) count * price * (1 + count) / 2;
        long answer = (money < cost) ? cost - money : 0;
        return answer;
    }
}