class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int sum_ab = Integer.parseInt("" + a + b);
        int ab2 = 2 * a * b;
        
        if (sum_ab < ab2) {
            answer = ab2;
        } else {
            answer = sum_ab;
        }
        
        return answer;
    }
}