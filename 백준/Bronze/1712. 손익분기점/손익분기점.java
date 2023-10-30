import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int A = scanner.nextInt();
		int B = scanner.nextInt();
		int C = scanner.nextInt();
		int answer = 0;
		if (B >= C) {
			answer = -1;
		} else {
			answer = (A / (C-B))+1;
		}
		System.out.println(answer);
	}	
}