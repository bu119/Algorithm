import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList<>();
        l -= 1;
        for (int i = l + (5 - l % 5); i <= r; i+=5) {
            String str = String.valueOf(i);
            boolean isValid = true;
            for (char ch : str.toCharArray()) {
                if (ch != '0' && ch != '5') {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                answer.add(i);
            }
        }
        if (answer.isEmpty()) {
            answer.add(-1);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
}