#include <iostream>
using namespace std;
int main() {
    int A,B,C;
    cin >> A >> B;
    cin >> C;
    cout << (A+((B+C)/60))%24 << " " << (B+C)%60 << endl;
    return 0;
}