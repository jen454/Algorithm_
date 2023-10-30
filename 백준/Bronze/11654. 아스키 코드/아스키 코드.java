import java.util.Scanner;

public class Main { // 아스키코드는 char를 byte로 강제변환

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		char c = scanner.next().charAt(0);
		byte num = (byte)c;
		System.out.println(num);
	}

}