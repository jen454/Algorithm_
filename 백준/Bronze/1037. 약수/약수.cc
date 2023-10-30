#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int N,sum=1,n;
    cin >> N;
    int Arr[N];
    for (int i=0; i<N; i++) {
        cin >> n;
        if (N==1) {
            cout << n*n << endl;
        }
        else {
            Arr[i] = n;
        }
    }
    sort(Arr,Arr+N);
    if (N!=1) cout << Arr[N-1]*Arr[0] << endl;
    return 0;
}