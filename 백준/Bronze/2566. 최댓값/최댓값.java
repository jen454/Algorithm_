import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int[][] Array = new int[10][10];
		int max = 0;
		int I = 0;
		int J = 0;
		for (int i=0; i<9; i++) {
			for (int j=0; j<9; j++) {
				Array[i][j] = scanner.nextInt();
			}
		}
		for (int i=0; i<9; i++) {
			for (int j=0; j<9; j++) {
				if (Array[i][j] > max) {
					max = Array[i][j];
					I = i;
					J = j;
				}
			}
		}
		System.out.println(max);
		System.out.println((I+1) + " " + (J+1));
	}

}