class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int x, y, temp;
        for (int i = 0; i < queries.length; i++) {
            x = queries[i][0];
            y = queries[i][1];
            temp = arr[x];
            arr[x] = arr[y];
            arr[y] = temp;
        }
        return arr;
    }
}