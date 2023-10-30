#include <iostream>
using namespace std;
int main() {
    int T,y=0,k=0,Y,K;
    cin >> T;
    for (int j=0; j<T; j++) {
        for (int i=0; i<9; i++) {
            cin >> Y >> K;
            y += Y;
            k += K;
        }
        if (y>k) cout << "Yonsei" << endl;
        else if (y<k) cout << "Korea" << endl;
        else cout << "Draw" << endl;
    }
    return 0;
}