class Solution {
    public String solution(String myString) {
		String answer = "";
        for (char ch : myString.toCharArray()) {
            if (ch == 'a') {
                answer += 'A';
            } else if (ch == 'A') {
                answer += ch;
            } else {
                answer += Character.toLowerCase(ch);
            }
        }
        return answer;
    }
}