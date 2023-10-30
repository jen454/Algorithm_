#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int N,K;
    cin >> N >> K;
    int arr[1001];
    for (int i=2; i<=N; i++) {
        arr[i] = i;
    }
    int cnt=0,num;
    for (int i=2; i<=N; i++) {
            for (int j = i; j<=N; j+=i) {
                if (cnt == K) break;
                if (arr[j] == 0) continue;
                num = arr[j];
                cnt++;
                arr[j] = 0;
            }
    }
    cout << num << endl;
    return 0;
}
// 2 4 6 3 5 7 / 2.xxx
// 2 4 6 8 10 12 14 3 9 15 5 7 11 13/ 3.xxx
// 2 4 6 8 10 3 9 5 7 / 3.xxx