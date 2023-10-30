#include <iostream>
using namespace std;
int main() {
    int A,B,sum=0,max=-1;
    for (int i=0; i<4; i++) {
        cin >> A >> B;
        sum -= A;
        sum += B;
        if (sum > max) {
            max = sum;
        }
    }
    cout << max << endl;
    return 0;
}