import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int M = scanner.nextInt();
		int[][] A = new int[N][M];
		int[][] B = new int[N][M];
		int[][] C = new int[N][M];
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				int X = scanner.nextInt();
				A[i][j] = X;
			}
		}
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				int Z = scanner.nextInt();
				B[i][j] = Z;
			}
		}
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				C[i][j] = A[i][j] + B[i][j];
			}
		}
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				System.out.print(C[i][j] + " ");
			}
			System.out.print("\n");
		}
	}
}
