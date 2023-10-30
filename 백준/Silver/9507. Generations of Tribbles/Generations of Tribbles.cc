#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    long long arr[68] = {1,1,2,4,};
    for (int i=0; i<64; i++) {
        arr[i+4] = (arr[i] + arr[i+1] + arr[i+2] + arr[i+3]);
    }

    int t,n;
    cin >> t;
    while (t) {
        cin >> n;
        cout << arr[n] << "\n";
        t--;
    }
    return 0;
}