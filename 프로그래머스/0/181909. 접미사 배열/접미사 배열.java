import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public String[] solution(String my_string) {
        ArrayList<String> answer = new ArrayList<>();
        // 접미사 만들기
        for (int i = 0; i < my_string.length(); i++) {
            answer.add(my_string.substring(i));
        }
        // 사전순 정렬
        Collections.sort(answer);
        // ArrayList → 배열 변환
        return answer.toArray(new String[0]);
    }
}