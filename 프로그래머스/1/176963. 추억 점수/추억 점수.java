import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        int n = photo.length;
        
        int[] answer = new int[n];
        
        Map<String, Integer> grades = new HashMap<>();
        
        for (int k = 0; k < name.length; k++) {
            grades.put(name[k], yearning[k]);
        }
        
        for (int i = 0; i < n; i++){
            // 각 열의 인덱스
            int m = photo[i].length;
            // 그리움 점수 합산
            int ssum = 0;
            
            for (int j = 0; j < m; j++){
                Integer grade = grades.get(photo[i][j]);
                if (grade != null) {
                    ssum += grade;
                }
            }
            answer[i] = ssum;
        }
        
        return answer;
    }
}