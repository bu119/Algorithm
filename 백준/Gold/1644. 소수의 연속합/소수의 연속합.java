import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static boolean isPrimeNum(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                // i로 나누어 떨어지면 소수가 아니므로 False
                return false;
            }
        }
        return true;
    }

    public static ArrayList<Integer> getPrimeArr(int n) {
        ArrayList<Integer> primeNum = new ArrayList<>();
        for (int num = 2; num <= n; num++) {
            if (isPrimeNum(num)) {
                primeNum.add(num);
            }
        }
        return primeNum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        ArrayList<Integer> arr = getPrimeArr(n);
        int start = 0;
        int end = 0;
        int ssum = 0;
        int cnt = 0;

        while (start < arr.size() && end <= arr.size()) {
            if (ssum >= n) {
                // 찾으려는 값보다 크거나 같을 때 맨 앞 값 제거
                ssum -= arr.get(start);
                start++;
            } else if (end == arr.size()) {
                break;

            } else {
                // 찾으려는 값보다 작을 때 뒤에 값 증가
                ssum += arr.get(end);
                end++;
            }
            // 부분합이 n일 때 카운트 증가
            if (ssum == n) {
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
