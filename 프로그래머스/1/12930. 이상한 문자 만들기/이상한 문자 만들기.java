class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        // 단어(공백을 기준)별로 짝/홀수 인덱스를 판단
        int wordIdx = 0;
        for (char c : s.toCharArray()) {
            if (c == ' ') {
                wordIdx = 0;
                sb.append(c);
            }
            else {
                sb.append(wordIdx % 2 == 0 ? Character.toUpperCase(c) : Character.toLowerCase(c));
                wordIdx++;
            }
        }
        return sb.toString();
    }
}
