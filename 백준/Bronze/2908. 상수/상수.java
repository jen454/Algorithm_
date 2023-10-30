import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		String A = Integer.toString(a);
		String B = Integer.toString(b);
		String AA = "";
		String BB = "";
		for (int i=0; i<3; i++) {
			AA += A.charAt(2-i);
			BB += B.charAt(2-i);
		}
		int AAA = Integer.parseInt(AA);
		int BBB = Integer.parseInt(BB);
		if (AAA > BBB) System.out.println(AAA);
		else System.out.println(BBB);
	}

}
