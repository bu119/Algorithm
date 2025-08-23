import java.util.*;

class Solution {
    public int solution(int[] array) {
        int n = array.length;
        Arrays.sort(array);
        int answer = array[n/2];
        return answer;
    }
}