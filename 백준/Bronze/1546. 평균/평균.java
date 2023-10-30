import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] Array = new int[N];
		double res = 0;
		for (int i=0; i<Array.length; i++) {
			int x = scanner.nextInt();
			Array[i] = x;
		}
		Arrays.sort(Array);
		for (int i=0; i<Array.length; i++) {
			res += (double)Array[i]/Array[Array.length-1]*100;
		}
		System.out.println(res / N);
	}

}
