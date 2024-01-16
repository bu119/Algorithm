import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
        int sumOdd = 0;
        int minOdd = 100;

        for (int i=0; i<7; i++) {
            int num = Integer.parseInt(bf.readLine()); //Int로 형변환
            if (num % 2 == 1) {
                sumOdd += num;
                if (num < minOdd) {
                    minOdd = num;
                }
            }
        }
        if (sumOdd == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sumOdd);
            System.out.println(minOdd);
        }
    }
}