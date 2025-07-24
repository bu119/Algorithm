import java.math.BigInteger;

class Solution {
    public int solution(String number) {
        BigInteger bigInt = new BigInteger(number);
        int answer = bigInt.mod(BigInteger.valueOf(9)).intValue();
        return answer;
    }
}