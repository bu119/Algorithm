class Solution {
    public int solution(int[][] sizes) {
        int maxW = 0;
        int maxH = 0;
        for (int[] size: sizes) {
            // 긴 쪽이 가로, 짧은 쪽이 세로 고정
            // 가로, 세로 각각 최대 길이 저장
			maxW = Math.max(Math.max(size[0], size[1]), maxW);
            maxH = Math.max(Math.min(size[0], size[1]), maxH);              
        }
        return maxW * maxH;
    }
}