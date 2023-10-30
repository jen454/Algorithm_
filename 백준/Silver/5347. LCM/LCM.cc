#include <iostream>
using namespace std;

long long gcd(long a, long b) {
if (a % b == 0) return b;
else return gcd(b, a % b);
}

long long lcm(long a, long b) {
    return a * b / gcd(a,b);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    long long a,b,n;
    cin >> n;
    while (n) {
        cin >> a >> b;
        cout << lcm(a,b) << "\n";
        n--;
    }
    return 0;
}