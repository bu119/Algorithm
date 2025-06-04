class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String str_ab = Integer.toString(a) + Integer.toString(b);
        String str_ba = Integer.toString(b) + Integer.toString(a);
        int int_ab =  Integer.valueOf(str_ab).intValue();
        int int_ba =  Integer.valueOf(str_ba).intValue();
        
        if (int_ab > int_ba) {
            answer = int_ab;
        } else {
            answer = int_ba;
        }
        return answer;
    }
}