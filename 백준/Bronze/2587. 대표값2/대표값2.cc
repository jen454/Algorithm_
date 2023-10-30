#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int arr[5] = {0,};
    int N,sum=0;
    for (int i=0; i<5; i++) {
        cin >> N;
        sum += N;
        arr[i] = N;
    }
    sort(arr,arr+5);
    cout << sum/5 << endl;
    cout << arr[2] << endl;
    return 0;
}