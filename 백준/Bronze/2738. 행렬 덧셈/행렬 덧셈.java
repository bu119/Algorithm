import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
        StringTokenizer st = new StringTokenizer(bf.readLine()); // StringTokenizer("문자열",구분자);
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] array = new int[n][m];
        for (int i=0; i < n; i++) {
            st = new StringTokenizer(bf.readLine()); // 한줄씩
            for (int j=0; j < m; j++) {
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < m; j++) {
                sb.append(array[i][j] + Integer.parseInt(st.nextToken()) + " ");
            }
        sb.append("\n");
        }
        System.out.println(sb);
    }
}