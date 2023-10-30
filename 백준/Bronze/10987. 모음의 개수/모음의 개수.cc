#include <iostream>
using namespace std;
int main() {
    int cnt=0;
    string s;
    cin >> s;
    for (int i=0; i<s.length(); i++) {
        if (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u') cnt++;
    }
    cout << cnt << endl;
    return 0;
}