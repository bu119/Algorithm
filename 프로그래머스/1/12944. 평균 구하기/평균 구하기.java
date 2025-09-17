import java.util.Arrays;

class Solution {
    public double solution(int[] arr) {
        int sum = Arrays.stream(arr).sum(); // 배열 합
        
        return (double) sum / arr.length;   // 평균
    }
}