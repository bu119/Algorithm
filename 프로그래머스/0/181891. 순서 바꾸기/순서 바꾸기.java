class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length;
        int[] answer = new int[len];
        
        int idx = 0;

        // 1. n번째 이후 원소들을 먼저 넣음
        for (int i = n; i < len; i++) {
            answer[idx++] = num_list[i];
        }

        // 2. n번째까지의 원소들을 이어붙임
        for (int i = 0; i < n; i++) {
            answer[idx++] = num_list[i];
        }

        return answer;
    }
}