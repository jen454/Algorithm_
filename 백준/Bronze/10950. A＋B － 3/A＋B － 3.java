import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		for (int i=0; i<N; i++) {
			int A = scanner.nextInt();
			int B = scanner.nextInt();
			System.out.println(A+B);
		}
	}

}
