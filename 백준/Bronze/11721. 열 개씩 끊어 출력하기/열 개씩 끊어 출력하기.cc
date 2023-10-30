#include <iostream>
using namespace std;
int main() {
    string s;
    cin >> s;
    int cnt = 0;
    for (int i=0; i<s.length(); i++) {
        cout << s[i];
        cnt++;
        if (cnt % 10 == 0) cout << "\n";
    }
    return 0;
}