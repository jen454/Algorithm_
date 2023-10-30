import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);	
		while (true) {
			int A = scanner.nextInt();
			int B = scanner.nextInt();
			
			if (A==0 && B==0) {
				scanner.close();
				break;
			}
			System.out.println(A+B);
		}
	}
}
