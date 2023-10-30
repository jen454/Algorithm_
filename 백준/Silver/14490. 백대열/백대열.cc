#include <iostream>
#include <string>
using namespace std;

int gcd2(int a, int b) {
    if (a % b == 0)
        return b;
    else
        return gcd2(b, a % b);
}

int main() {
    int n,m;
    char s;
    cin >> n >> s >> m;
    int gcd = gcd2(n,m);
    cout << n/gcd << ":" << m/gcd << endl;
    return 0;
}