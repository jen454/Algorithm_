#include <iostream>
using namespace std;
int main() {
    int min = 2001,n;
    for (int i=0; i<3; i++) {
        cin >> n;
        if (n < min) min = n;
    }
    int Min = 2001,N;
    for (int i=0; i<2; i++) {
        cin >> N;
        if (N < Min) Min = N;
    }
    cout << min + Min - 50 << endl;
    return 0;
}