import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 공의 개수
        int[] posi = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            posi[i] = Integer.parseInt(st.nextToken());
        }
        int t = Integer.parseInt(br.readLine()); // 시간

        Arrays.sort(posi);
        int cnt = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (posi[j] - posi[i] <= 2 * t) {
                    cnt++;
                }
            }
        }

        System.out.println(cnt / 4.0);
    }
}
