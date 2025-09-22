class Solution {
    public long solution(int price, int money, int count) {
        // 총 놀이기구 비용 = price × (1 + ... + count)
        // 등차수열의 합 공식: n × (n + 1) / 2
        long cost = (long) count * price * (1 + count) / 2;
        // 부족한 금액만 반환 (부족하지 않으면 0)
        return Math.max(0, cost - money);
    }
}
