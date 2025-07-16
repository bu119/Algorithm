class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int n = queries.length;
        int[] answer = new int[n];
        int s, e, k, min_v;
        int m = arr.length;
        for (int i = 0; i < n; i++) {
            s = queries[i][0];
        	e = queries[i][1];
            k = queries[i][2];
            min_v = 1000001;
            for (int j = s; j < Math.min(m, e+1); j++) {
                if (k < arr[j] && arr[j] < min_v) {
                    min_v = arr[j];
                }
            }
            if (min_v == 1000001) {
                min_v = -1;
            }
            answer[i] = min_v;
        }
        return answer;
    }
}