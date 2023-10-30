#include <iostream>
using namespace std;
int main() {
    int A,B;
    int a,b,c;
    cin >> A >> B;
    a = B % 10;
    b = (B/10)%10;
    c = (B/10)/10;
    cout << a*A << endl;
    cout << b*A << endl;
    cout << c*A << endl;
    cout << A*B << endl;
    return 0;
}