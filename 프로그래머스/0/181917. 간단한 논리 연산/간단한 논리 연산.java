class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = false;
        boolean l = true;
        boolean r = true;
        
        if (x1 == false && x2 == false) {
            l = false;
        } 
        
        if (x3 == false && x4 == false) {
            r = false;
        } 
            
        if (l == true && r == true) {
            answer = true;
        }
        
        return answer;
    }
}