#include <iostream>
using namespace std;
int main() {
    int N,K,cnt=0;
    cin >> N >> K;
    int arr[11];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }    
    for (int i=N-1; i>=0; i--) {
        cnt += K/arr[i];
        K = K%arr[i];
    }
    cout << cnt << endl;
    return 0;
}