import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int[] Array = new int[10];
		int max = Array[0];
		int max_index = 0;
		for (int i=1; i<10; i++) {
			int n = scanner.nextInt();
			Array[i] = n;
		}
		for (int i=1; i<10; i++) {
			if (Array[i] > max) {
				max = Array[i];
				max_index = i;
			}
		}
		System.out.println(max);
		System.out.println(max_index);
	}

}
