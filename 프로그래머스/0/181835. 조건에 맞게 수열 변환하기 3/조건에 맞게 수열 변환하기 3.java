class Solution {
    public int[] solution(int[] arr, int k) {
        int n = arr.length;
        int[] answer = new int[n];
        for (int i = 0; i < arr.length; i++) {
            if (k%2 == 1) {
                answer[i] = arr[i]*k;
            } else {
                answer[i] = arr[i]+k;
            }
        }
        return answer;
    }
}