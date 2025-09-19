import java.util.*;

class Solution {
    public String solution(String s) {
        // 문자열을 문자 배열로 변환
        char[] arr = s.toCharArray();
        // 오름차순 정렬
        Arrays.sort(arr);
        // StringBuilder로 문자열 만든 후 뒤집기
        StringBuilder sb = new StringBuilder(new String(arr));
        // 뒤집어서 내림차순 반환
        return sb.reverse().toString();
    }
}