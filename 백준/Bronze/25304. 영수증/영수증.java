import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int X = scanner.nextInt();
		int N = scanner.nextInt();
		int sum = 0;
		for (int i=0; i<N; i++) {
			int a = scanner.nextInt();
			int b = scanner.nextInt();
			sum += a*b;
		}
		if (X == sum) System.out.print("Yes");
		else System.out.print("No");
	}

}
