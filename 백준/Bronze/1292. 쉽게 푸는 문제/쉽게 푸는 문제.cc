#include <iostream>
using namespace std;
int main() {
    int A,B,idx=1,sum=0;
    int arr[1001] ={0,};
    cin >> A >> B;
    for (int i=1; i<1001; i++) {
        for (int j=1; j<=i; j++) {
            arr[idx] = i;
            if (idx>1000) break;
            idx++;
        }
    }
    for (int i=A; i<=B; i++) {
        sum += arr[i];
    }
    cout << sum << endl;
    return 0;
}