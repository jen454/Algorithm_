#include <iostream>
using namespace std;

int main() {
	int N;
    long long TN[36] = {0,};
	cin >> N;
	TN[0] = 1;
	for (int i = 1; i < N + 1; i++) {
		for (int j = 0; j < i; j++) {
			TN[i] += TN[j] * TN[i - j - 1];
		}
	}
	cout << TN[N];
	return 0;
}