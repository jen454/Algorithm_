#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int N,num;
    cin >> N;
    int arr[N];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }
    sort(arr,arr+N,greater<int>());
    for (int i:arr) {
        cout << i << "\n";
    }
    return 0;
}