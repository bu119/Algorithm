import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] nk = reader.readLine().split(" ");
        char[] arr = reader.readLine().toCharArray();
//        String[] arr = reader.readLine().split("");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);
        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] == 'P') {
                int s = Math.max(0, i - k);
                int e = Math.min(n - 1, i + k);

                for (int j = s; j <= e; j++) {
                    if (arr[j] == 'H') {
                        arr[j] = 'X';
                        ans++;
                        break;
                    }
                }
            }
        }

        System.out.println(ans);
    }
}