#include <iostream>
using namespace std;
int main() {
    int N,fac=1;
    cin >> N;
    if (N==0) {
        cout << 1 << endl;
    }
    else {
        for (int i=1; i<=N; i++) {
            fac *= i;
        }
        cout << fac << endl;
    }
    return 0;
}