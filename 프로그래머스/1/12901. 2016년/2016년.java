class Solution {
    public String solution(int a, int b) {
        
        String[] dayOfWeek = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        int[] daysInMonth = {31,29,31,30,31,30,31,31,30,31,30,31};
        // a월 b일까지 총 며칠 지났는지 저장 (1일 기준 시작)
        int totalDays = b - 1;
        
        for (int i = 0; i < a - 1; i++) {
            totalDays += daysInMonth[i];
        }        
                
        return dayOfWeek[totalDays % 7];
    }
}