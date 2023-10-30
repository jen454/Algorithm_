#include <iostream>
using namespace std;
int main() {
    int T,A,B;
    cin >> T;
    for (int i=0; i<T; i++) { 
        cin >> A >> B;
        cout << "You get " << A/B << " piece(s) and your dad gets " << A%B << " piece(s)." << endl;
    }
    return 0;
}