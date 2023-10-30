#include <iostream>
using namespace std;
int main() {
    int h,m,s,t;
    cin >> h >> m >> s;
    cin >> t;
    s += t;
    m += s/60;
    h += m/60;
    cout << h%24 << " " << m%60 << " " << s%60 << endl;
    return 0;
}