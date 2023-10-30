import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int[] Array = new int[10];
		boolean ans;
		int count = 0;
		for (int i=0; i<10; i++ ) {
			int n = scanner.nextInt();
			Array[i] = n%42;
		}
		for (int i=0; i<10; i++) {
			ans = false;
			for (int j=i+1; j<10; j++) {
				if (Array[i] == Array[j]) {
					ans = true;
					break;
				}
			}
			if (ans == false) {
				count++;
			}
		}
		System.out.println(count);
	}
}
