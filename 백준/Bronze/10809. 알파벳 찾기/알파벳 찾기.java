import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String S = sc.next();
		int[] num = new int[26];
		for (int i=0; i<26; i++) {
			num[i] = -1;
		}
		for (int i=0; i<S.length(); i++) {
			char c = S.charAt(i);
			if (num[c - 'a'] == -1) {
				num[c - 'a'] = i;
			}
		}
		for (int i=0; i<26; i++) {
			System.out.print(num[i] + " ");
		}
	}
}
