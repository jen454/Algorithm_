#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int sum=0,n;
    int arr[9] = {0,};
    int Arr[9] = {0,};
    for (int i=1; i<9; i++) {
        cin >> n;
        arr[i] = n;
        Arr[i] = n;
    }
    sort(arr,arr+9);
    for (int i=4; i<9; i++) {
        sum += arr[i];
    }
    cout << sum << endl;
    for (int i=0; i<9; i++) {
        if (Arr[i] == arr[4] || Arr[i] == arr[5] || Arr[i] == arr[6] || Arr[i] == arr[7] || Arr[i] == arr[8]) {
            cout << i << " ";
        }
    }
    cout << "\n";
    return 0;
}