import java.util.Arrays;
import java.util.Scanner;

/**
 * 2217
 */
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] num = new int[N];
        int[] sum = new int[N];
        for (int i=0; i<N; i++) {
            int n = sc.nextInt();
            num[i] = n;
        }
        Arrays.sort(num);
        for (int i=0; i<N; i++) {
            sum[i] = (N-i) * num[i];
        }
        Arrays.sort(sum);
        System.out.println(sum[N-1]);
    }
}