#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int K,N;
    int arr[51];
    cin >> K;
    for (int i=1; i<=K; i++) {
        cin >> N;
        for (int j=0; j<N; j++) {
            cin >> arr[j];
        }
        sort(arr,arr+N,greater<int>());
        int lg=0;
        for (int j=1; j<N; j++) {
            if (arr[j-1]-arr[j] > lg) {
                lg = arr[j-1]-arr[j];
            }
        }
        cout << "Class " << i << endl;
        cout << "Max " << arr[0] << ", Min " << arr[N-1] << ", Largest gap " << lg << endl;
    }
    return 0;
}