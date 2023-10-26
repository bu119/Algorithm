class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        while (!s.equals("1")) {
            int originalLength = s.length();
            s = s.replaceAll("0", ""); // 0을 제거
            int newLength = s.length();
            int removedZeros = originalLength - newLength; // 제거된 0의 개수
            s = Integer.toBinaryString(newLength); // 길이를 2진법 문자열로 변환
            answer[0]++; // 이진 변환 횟수 증가
            answer[1] += removedZeros; // 제거된 0의 개수 누적
        }

        return answer;
    }
}