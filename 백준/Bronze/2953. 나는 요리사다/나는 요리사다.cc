#include <iostream>
using namespace std;
int main() {
    int a,b,c,d,max=-1;        
    int idx = 0;
    for (int i=1; i<=5; i++) {
        int sum = 0;
        cin >> a >> b >> c >> d;
        sum += a+b+c+d;
        if (sum > max) {
            max = sum;
            idx = i;
        }
    }
    cout << idx << " " << max << endl;
    return 0;
}