import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int m = Integer.toString(n).length();
        
        for (int i = m - 1; i >= 0; i--) {
            answer += n / Math.pow(10, i);
            n %= Math.pow(10, i);
        }
        
        return answer;
    }
}