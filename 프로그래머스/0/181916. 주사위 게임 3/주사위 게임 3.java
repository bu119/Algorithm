import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {

        int[] number = {a, b, c, d};
        Arrays.sort(number); // 오름차순
        
        // 4개 모두 다름: 최솟값
        int answer = number[0]; 

        if (number[0] == number[3]) {	// 4개 모두 같음: pppp
            answer = 1111 * a;
        } else if (number[0] == number[2]) {	// 3+1: pppq
            answer = (10 * number[0] + number[3]) * (10 * number[0] + number[3]);
        } else if (number[1] == number[3]) {	// 3+1: qppp
        	answer = (10 * number[1] + number[0]) * (10 * number[1] + number[0]);
        } else if (number[0] == number[1] && number[2] == number[3]) {	// 2+2: ppqq
            answer = (number[0]+number[2]) * Math.abs(number[0]-number[2]);
        } else if (number[0] == number[1]) {	// 2+1+1: ppqr
            answer = number[2] * number[3];
        } else if (number[1] == number[2]) {	// 2+1+1: qppr
            answer = number[0] * number[3];
        } else if (number[2] == number[3]) {	// 2+1+1:qrpp
            answer = number[0] * number[1];
        }        
        // 4개 모두 다름: 최솟값
        return answer;
    }
}