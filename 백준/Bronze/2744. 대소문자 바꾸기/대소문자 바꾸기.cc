#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    cin >> s;
    for (int i=0; i<s.length(); i++) {
        if (s[i]-'A'>=0 && s[i]-'A'<=25) cout << (char)(int(s[i])+32);
        if (s[i]-'a'>=0 && s[i]-'a'<=25) cout << (char)(int(s[i])-32);
    }
    return 0;
}