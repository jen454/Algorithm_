#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int w=0,k=0;
    int warr[10],karr[10];
    for (int i=0; i<10; i++) {
        cin >> warr[i];
    }
    sort(warr,warr+10);
    for (int i=0; i<10; i++) {
        cin >> karr[i];
    }
    sort(karr,karr+10);
    w += warr[7] + warr[8] + warr[9];
    k += karr[7] + karr[8] + karr[9];
    cout << w << " " << k << endl;
    return 0;
}