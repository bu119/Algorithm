class Solution {
    public int[] solution(int[] arr) {
        // 배열의 크기
        int n = arr.length;
            
        int[] answer = new int[n];
        
        for (int i = 0; i < n; i++) {

            if (50 <= arr[i] & arr[i] % 2 == 0) {
                arr[i] /= 2;
            } 
            else if (50 > arr[i] & arr[i] % 2 == 1) {
                arr[i] *= 2;                
            }

            answer[i] = arr[i];

        }
        
        return answer;
    }
}