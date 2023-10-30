import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String S = sc.next();
		String str = S.toUpperCase();
		int[] Array = new int[26];
		int Max = Array[0];
		char ch = '?';
		
		for (int i=0; i<26; i++) {
			Array[i] = 0;
		}
		
		for (int i=0; i<str.length(); i++) {
			Array[(str.charAt(i) - 'A')]++;
		}
		
		for (int i=0; i<26; i++) {
			if (Array[i] > Max) {
				Max = Array[i];
				ch = (char) (i + 65);
				}
			else if (Array[i] == Max) {
				ch = '?';
			}
		}
		System.out.println(ch);
	}
}