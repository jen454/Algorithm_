import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int n = han(N);
		System.out.println(n);
	}
	
	public static int han(int number) {
		int count = 0;
		for (int i=1; i<=number; i++) {
			if (i>=1 && i<100) count++;
			else if (i>=100) {
				int one = i % 10;
				int two = (i / 10) % 10;
				int thr = (i / 10) / 10;
				if ((two - thr) == (one - two)) {
					count++;
				}
			}
		}
		return count;
	}
}
