#include <iostream>
using namespace std;
int main() {
    int T,s,n,q,p,sum;
    cin >> T;
    for (int i=0; i<T; i++) {
        sum = 0;
        cin >> s >> n;
        sum += s;
        for (int i=0; i<n; i++) {
            cin >> q >> p;
            sum += q*p;
        }
        cout << sum << endl;
    }
    return 0;
}