#include <iostream>
#include <string>
using namespace std;
int main() {
    string str;
    int cnt=0;
    cin >> str;
    for (int i=0; i<str.size(); i++) {
        if (str[i] != str[str.size()-i-1]) {
            cout << 0 << endl;
            break;
        }
        cnt++;
    }
    if (cnt == str.size()) cout << 1 << endl;
    return 0;
}