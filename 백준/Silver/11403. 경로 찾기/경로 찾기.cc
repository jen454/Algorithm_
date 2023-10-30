#include <iostream>
using namespace std;
#define MAX 100

int arr[MAX][MAX];

int main() {
    int N;
    cin >> N;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			for (int k=0; k<N; k++) {
				if (arr[j][i] && arr[i][k]) {
					arr[j][k] = 1;
				}
			}
		}
	}

	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			cout << arr[i][j] << ' ';
		}
		cout << '\n';
	}
    
    return 0;
}