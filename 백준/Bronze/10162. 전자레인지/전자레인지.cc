#include <iostream>
using namespace std;
int main() {
    int T,A=0,B=0,C=0;
    cin >> T;
    if (T % 10 !=0) cout << -1 << endl;
    else {
        A = T/300;
        B = (T%300)/60;
        C = (T%300)%60/10;
        cout << A << " " << B << " " << C << endl;
    }
    return 0;
}