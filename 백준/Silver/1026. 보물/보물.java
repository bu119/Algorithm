import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] a = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] b = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(a);
        Arrays.sort(b);
        // Arrays.sort(b, Collections.reverseOrder());
        int ssum = 0;
        for (int i = 0; i < n; i++) {
            ssum += a[i] * b[n - i - 1];
        }
        System.out.println(ssum);
    }
}