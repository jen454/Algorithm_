import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int count = 0;
		for (int i=0; i<N; i++) {
			boolean is = true;
			int X = scanner.nextInt();
			if (X==1) continue;
			for (int j=2; j<=Math.sqrt(X); j++) {
				if (X % j == 0) {
					is = false;
					break;
				}
			}
			if(is) {
				count++;
			}
		}
		System.out.println(count);
	}

}
