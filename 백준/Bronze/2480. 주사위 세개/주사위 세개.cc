#include <iostream>
using namespace std;
int main() {
    int A,B,C;
    cin >> A >> B >> C;
    int sum = 0;
		if (A==B && B==C) sum = 10000+(A*1000);
		else if (A==B && B!=C) sum = 1000+(A*100);
		else if (B==C && C!=A) sum = 1000+(B*100);
		else if (A==C && A!=B) sum = 1000+(C*100);
		else if (A!=B && B!=C) {
			if (A>B && A>C) 
				sum = A*100;
			else if (B>A && B>C) 
				sum = B*100;
			else if (C>A && C>B)
				sum = C*100;
		}
    cout << sum << endl;
    return 0;
}