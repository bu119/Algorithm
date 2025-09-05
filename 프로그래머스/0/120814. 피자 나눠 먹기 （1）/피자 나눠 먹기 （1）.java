class Solution {
    public int solution(int n) {
        // 1) n명을 7로 나눠서, 피자(7)가 몇 개 필요한지 확인
        // 2) n명을 7로 나눈 나머지가 존재하면 피자 개수 + 1
        int answer = (n % 7 == 0)? n/7 : n/7+1;
        return answer;
    }
}