#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    int arr[N];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }  
    sort(arr,arr+N,greater<int>());
    cout << arr[K-1] << endl;
    return 0;
}