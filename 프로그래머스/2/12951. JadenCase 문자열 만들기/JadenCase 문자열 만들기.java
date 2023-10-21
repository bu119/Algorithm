class Solution {
    public String solution(String s) {
        String answer = "";
        String[] sLower = s.toLowerCase().split("");
        // 이전 공백 체크
        boolean flag = true;

        for(String sp : sLower) {
            
            if (flag) {
                answer += sp.toUpperCase();
            } else {
                answer += sp;
            }

            flag = sp.equals(" ") ? true : false;
        }

        return answer;
    }
}