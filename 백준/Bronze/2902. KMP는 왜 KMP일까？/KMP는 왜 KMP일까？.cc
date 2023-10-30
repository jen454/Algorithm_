#include <iostream>
using namespace std;
int main() {
    string str,s="";
    cin >> str;
    s += str[0];
    for (int i=0; i<str.size(); i++) {
        if (str[i] == '-') s += str[i+1];
    }
    cout << s << endl;
    return 0;
}