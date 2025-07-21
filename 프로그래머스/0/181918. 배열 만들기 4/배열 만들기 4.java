import java.util.Stack;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>();
        int n = arr.length;
        int i = 0;
        while (i < n) {
        	if (stk.isEmpty() || stk.peek() < arr[i]) {
            	stk.push(arr[i]);
                i += 1;
            } else {               
                stk.pop();
            }
        }  
        return stk.stream().mapToInt(Integer::intValue).toArray();
    }
}