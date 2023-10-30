import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int A = scanner.nextInt();
		int B = scanner.nextInt();
		if (A>B) System.out.print(">");
		else if (A<B) System.out.print("<");
		else System.out.print("==");
	}

}
