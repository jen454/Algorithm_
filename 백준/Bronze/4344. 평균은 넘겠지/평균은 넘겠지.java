import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		
		for (int i=0; i<N; i++) {
			double sum = 0;
			double num = 0;
			int cnt = 0;
			int X = scanner.nextInt();
			int[] arr = new int[X];
			for (int j=0; j<X; j++) {
				int Y = scanner.nextInt();
				arr[j] = Y;
				num += arr[j];
			}
			sum = (double)num/X;
			for (int j=0; j<X; j++) {
				if (arr[j] > sum) {
					cnt++;
				}
			}
			System.out.println(String.format("%.3f", ((double)cnt / X * 100)) + "%");
		}
	}

}
