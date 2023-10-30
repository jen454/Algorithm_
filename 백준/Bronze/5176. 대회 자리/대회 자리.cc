#include <iostream>
using namespace std;
int main() {
    int K;
    cin >> K;
    for (int i=0; i<K; i++) {
        int P,M,cnt=0;
        cin >> P >> M;
        int arr[501] = {0,};
        for (int i=0; i<P; i++) {
            int n;
            cin >> n;
            arr[n]++;
            if (arr[n] > 1) cnt++;
        }
        cout << cnt << endl;
    }
    return 0;
}