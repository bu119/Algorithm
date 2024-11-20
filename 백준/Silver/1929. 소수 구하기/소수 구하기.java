import java.util.*;

public class Main {
    // 소수 판별 함수
    public static boolean isPrimeNumber(int number){
        // 1은 소수가 아님
        if (number == 1) {
            return false;
        }
        // 2부터 √k까지 확인
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // 입력 받기
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        // m부터 n까지의 소수 출력
        for (int num = m; num <= n; num++) {
            if (isPrimeNumber(num)) {
                System.out.println(num);
            }
        }
        scanner.close();
    }
}