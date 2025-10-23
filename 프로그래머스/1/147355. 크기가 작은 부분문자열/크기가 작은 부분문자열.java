class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        // 길이 찾기
        int n = t.length();
        int m = p.length();
        // long으로 변환
        long pNum = Long.parseLong(p);
        // p길이의 부분문자열을 찾아서 숫자 비교
        for (int i = 0; i < n-m+1; i++) {
            // long으로 변환
            long tSubNum = Long.parseLong(t.substring(i,i+m));
            // 크기 비교
            if (tSubNum <= pNum) {
                answer++;
            }
        }
        return answer;
    }
}