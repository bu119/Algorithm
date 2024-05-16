class Solution {
    int solution(int[][] land) {
        int n = land.length;

        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < 4; j++) {
                int maxV = 0;
                for (int k = 0; k < 4; k++) {
                    if (k!=j && maxV < land[i][k]) {
                         maxV = land[i][k];
                    }
                }
                land[i+1][j] += maxV;
            }
        }
        
        int answer = land[n-1][0];
        for (int j = 1; j < 4; j++) {
            if (answer < land[n-1][j]) {
                answer = land[n-1][j];
            }
        }
        return answer;
    }
}