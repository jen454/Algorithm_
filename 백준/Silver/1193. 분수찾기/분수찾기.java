import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int cross_count = 1, prev_count_sum = 0;
		while(true) {
			if (x <= prev_count_sum + cross_count) {
				if (cross_count % 2 == 1) {
					System.out.print((cross_count - (x - prev_count_sum -1) + "/" + (x - prev_count_sum)));
					break;
				}
				else {
					System.out.print((x - prev_count_sum) + "/" + (cross_count - (x - prev_count_sum - 1)));
					break;
				}
			}
			else {
				prev_count_sum += cross_count;
				cross_count++;
			}
		}
	}
}

// 1/1 합2 / 1
// 1/2 2/1 합3 / 2 3
// 3/1 2/2 1/3 합4 / 4 5 6
// 1/4 2/3 3/2 4/1 합5 / 7 8 9 10
// 5/1 4/2 3/3 2/4 1/5 합6 / 11 12 13 14 15
// 1/6 2/5 3/4 4/3 5/2 6/1 합7 / 16 17 18 19 20 21