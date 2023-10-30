#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int t,n;
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> n;
        int arr[n];
        for (int j=0; j<n; j++) {
            cin >> arr[j];
        }
        sort(arr,arr+n);
        cout << 2*(arr[n-1]-arr[0]) << endl;
    }
    return 0;
}