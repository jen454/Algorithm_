#include <iostream>
#include <set>
using namespace std;
int main() {
    string s,str="";
    cin >> s;
    set<string> set;
    for (int i=0; i<s.length(); i++) {
        for (int j=i; j<s.length(); j++) {
            str += s[j];
            set.insert(str);
        }
        str = "";
    }
    cout << set.size() << endl;
    return 0;
}