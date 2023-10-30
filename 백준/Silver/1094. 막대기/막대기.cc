#include <iostream>
using namespace std;
int main() {
    int cnt=1,x,num=64,base=64;
    cin >> x;
    while(num > x) {
        base /= 2;
        if (num-base >= x) num-=base;
        else cnt++;
    }
    cout << cnt << endl;
    return 0;
}