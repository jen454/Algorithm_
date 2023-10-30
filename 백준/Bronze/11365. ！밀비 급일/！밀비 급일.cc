#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    while (true) {
        getline(cin,s);
        if (s == "END") break;
        for (int i=s.length()-1; i>=0; i--) {
            cout << s[i];
        }
        cout << "\n";
    }
    return 0;
}