import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] Array = new int[N];
		int max = -1000000;
		int min = 1000000;
		for (int i=0; i<N; i++) {
			int x = scanner.nextInt();
			Array[i] = x;
		}
		for (int i=0; i<N; i++) {
			if (Array[i] > max) {
				max = Array[i];
			}
			if (Array[i] < min) {
				min = Array[i];
			}
		}
		System.out.println(min + " " + max);
	}

}
