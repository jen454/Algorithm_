#include <iostream>
using namespace std;
int main() {
    int A,B,C,D,E;
    cin >> A >> B >> C >> D >> E;
    if (A < 40) A = 40;
    if (B < 40) B = 40;
    if (C < 40) C = 40;
    if (D < 40) D = 40;
    if (E < 40) E = 40;
    int sum = A+B+C+D+E;
    cout << sum / 5 << endl;
    return 0;
}