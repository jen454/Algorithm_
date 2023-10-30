import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int X = scanner.nextInt();
		int[] Array = new int[N];
		for (int i=0; i<N; i++) {
			int A = scanner.nextInt();
			Array[i] = A;
		}
		for (int i=0; i<Array.length; i++) {
			if (Array[i] < X) {
				System.out.print(Array[i] + " ");
			}
		}
	}

}
