import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] number = {a, b, c, d};
        Arrays.sort(number); // 오름차순
        
        // 4개 모두 같음: pppp
        if (number[0] == number[3]) {
            return 1111 * a;
        }
        // 3+1: pppq / qppp
        if (number[0] == number[2]) {
            return (10 * number[0] + number[3]) * (10 * number[0] + number[3]);
        }
        if (number[1] == number[3]) {
        	return (10 * number[1] + number[0]) * (10 * number[1] + number[0]);
        } 
        
        // 2+2: ppqq
        if (number[0] == number[1] && number[2] == number[3]) {
            return (number[0]+number[2]) * Math.abs(number[0]-number[2]);
        }
        
        // 2+1+1: ppqr / qppr / qrpp
        if (number[0] == number[1]) {
            return number[2] * number[3];
        }
        if (number[1] == number[2]) {
            return number[0] * number[3];
        }        
        if (number[2] == number[3]) {
            return number[0] * number[1];
        }        
        
        // 4개 모두 다름: 최솟값
        return number[0];
    }
}