#include <iostream>
using namespace std;
int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int sum=0,n,min=101;
        for (int j=0; j<7; j++) {
            cin >> n;
            if (n%2==0) {
                sum += n;
                if (n < min) min = n;
            }
        }
        cout << sum << " " << min << endl;
    }
    return 0;
}