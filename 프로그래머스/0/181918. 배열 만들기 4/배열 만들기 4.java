import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList<>();
        int n = arr.length;
        int i = 0;
        while (i < n) {
            int m = stk.size();
        	if (stk.isEmpty() || stk.get(m-1) < arr[i]) {
            	stk.add(arr[i]);
                i += 1;
            } else {               
                stk.remove(m - 1);
            }
        }  
        return stk.stream().mapToInt(Integer::intValue).toArray();
    }
}