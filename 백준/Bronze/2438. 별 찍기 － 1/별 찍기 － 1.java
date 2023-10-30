import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		for (int i=1; i<N+1; i++) { 
			for (int j=0; j<i; j++) {
				System.out.print('*');
			}
			System.out.print("\n");
		}
	}

}
