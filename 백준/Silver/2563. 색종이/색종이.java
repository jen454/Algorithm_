import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		boolean[][] Square = new boolean[100][100];
		int cnt = 0;
		for (int i=0; i<N; i++) {
			int x = scanner.nextInt();
			int y = scanner.nextInt();
			for (int j=x; j<x+10; j++) {
				for (int k=y; k<y+10; k++) {
					Square[j][k] = true;
				}
			}
		}
		for (int j=0; j<Square.length; j++) {
			for (int k=0; k<Square.length; k++) {
				if (Square[j][k] == true) {
					cnt++;
				}
			}
		}
		System.out.println(cnt);
	}
}
