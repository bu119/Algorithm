class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int diff = 101;
        for (int i = 0;i < array.length;i++) {
            int ndiff = Math.abs(array[i] - n);
            if (ndiff < diff) {
                diff = ndiff;
                answer = array[i];
            } else if (ndiff == diff && array[i] < answer) {
                answer = array[i];
            }
        }
        return answer;
    }
}