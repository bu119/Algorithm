class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        // p 길이 찾기
        int n = t.length();
        int m = p.length();
        long p_num = Long.parseLong(p);
        // t에서 p 길이만큼 부분 문자열을 찾아,숫자 비교
        for (int i = 0; i < n-m+1; i++) {
            if (Long.parseLong(t.substring(i,i+m)) <= p_num) {
                answer++;
            }
        }
        return answer;
    }
}