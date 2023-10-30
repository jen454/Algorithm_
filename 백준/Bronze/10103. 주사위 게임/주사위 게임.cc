#include <iostream>
using namespace std;
int main() {
    int T,A=100,B=100,a,b;
    cin >> T;
    for (int i=0; i<T; i++) {
        cin >> a >> b;
        if (a>b) {
            B -= a;
        } 
        else if (a<b) {
            A -= b;
        }
    }
    cout << A << endl;
    cout << B << endl;
    return 0;
}