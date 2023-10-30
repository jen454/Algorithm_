import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int[] Array = new int[31];
		for (int i=1; i<29; i++) {
			int n = scanner.nextInt();
			Array[n] = 1;
		}
		for (int i=1; i<Array.length; i++) {
			if (Array[i] != 1) {
				System.out.println(i);
			}
		}
	}

}
