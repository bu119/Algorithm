import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
        int n = Integer.parseInt(bf.readLine()); //정수로 형변환

        for (int i = 0; i < n; i++) {
            //공백 출력
            for (int j = 0; j < i; j++){
                System.out.print(" ");
            }
            //별표 출력
            for (int k = i ; k < n; k++) {
                System.out.print("*");
            }
            // 각 행이 끝난 후 다음 줄로 이동
            System.out.println();
        }
    }
}