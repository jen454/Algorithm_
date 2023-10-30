import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int sum = A*B*C;
		int[] num = new int[10];
		while (sum / 10 != 0) {
			num[sum%10]++;
			sum /= 10;
		}
		num[sum]++;
		for (int i=0; i<num.length; i++) {
			System.out.println(num[i]);
		}
	}
	
}
