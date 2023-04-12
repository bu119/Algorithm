import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    // 입력 데이터 읽기
    // String str = reader.readLine();  // Hi Anna

    // 입력 데이터 출력
    // System.out.println(str);  // Hi Anna
    String[] str = reader.readLine().split(" ");
    int A = Integer.parseInt(str[0]);
    int B = Integer.parseInt(str[1]);

    System.out.println(A+B);
    System.out.println(A-B);
    System.out.println(A*B);
    System.out.println(A/B);
    System.out.println(A%B);
  }

}