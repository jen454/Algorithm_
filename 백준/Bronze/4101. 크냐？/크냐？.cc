#include <iostream>
using namespace std;
int main() {
    int A,B;
    while(true) {
        cin >> A >> B;
        if (A == 0 && B == 0) break;
        if (A>B) {
            cout << "Yes" << endl;
        }
        else cout << "No" << endl;
    }
    return 0;
}