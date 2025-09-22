class Solution {
    public long solution(int price, int money, int count) {
        long cost = (long) count * price * (1 + count) / 2;

        return Math.max(0, cost-money);
    }
}