// 1 : 0 1 / 2 : 1 1 / 3 : 1 2 / 4 : 2 3 / 5 : 3 5 / ... / 10 : 34 55

#include <iostream>
using namespace std;
int main() {
    int k,A=1,B=0;
    cin >> k;
    while(k) {
        int tmp = A;
        A = B;
        B += tmp;
        k--;
    }
    cout << A << " " << B << endl;
    return 0;
}