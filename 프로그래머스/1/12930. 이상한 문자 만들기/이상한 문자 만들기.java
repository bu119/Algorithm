class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        // 단어(공백을 기준)별로 짝/홀수 인덱스를 판단
        int wordIdx = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i); // i번째 문자 꺼내기
            if (c == ' ') {
                wordIdx = 0;
                sb.append(c);
            }
            else if (wordIdx % 2 == 0) {
                sb.append(Character.toUpperCase(c));
                wordIdx += 1;
            } else {
                sb.append(Character.toLowerCase(c));
                wordIdx += 1;
            }
        }
        return sb.toString();
    }
}
