class Solution {
    public String solution(String s) {

        String[] arr = s.split(" ");
        
        int maxV = Integer.parseInt(arr[0]);
        int minV = Integer.parseInt(arr[0]);
        
        for (int i=1; i < arr.length;i++){
            
            int num = Integer.parseInt(arr[i]);
            
            if (maxV < num) {
                maxV = num;
            }
            if (minV > num) {
                minV = num;
            }
        }
        
        return  minV + " " + maxV;
    }
}