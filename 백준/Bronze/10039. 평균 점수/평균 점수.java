import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언

        int ssum = 0;
        for (int i = 0; i < 5; i++) {
            int score = Integer.parseInt(bf.readLine());
            if (score < 40) {
                ssum += 40;
                continue;
            }
            ssum += score;
        }
        System.out.println(ssum/5);
    }
}