import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int cnt = 0;
		int num = N;
		while (true) {
			N = ((N%10)*10) + (((N/10)+(N%10))%10);
			cnt++;
			if (num == N) {
				break;
			}
		}
		System.out.println(cnt);
	}

}
