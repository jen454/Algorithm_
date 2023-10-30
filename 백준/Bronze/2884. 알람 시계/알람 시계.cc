#include <iostream>
using namespace std;
int main() {
    int H,M,X;
    cin >> H >> M;
    X = M-45;
    if (M-45<0) {
        X = 60+(M-45);
        H--;
        if (H<0) H = 23;
    }
    cout << H << " " << X << endl;
    return 0;
}