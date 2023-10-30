#include <iostream>
using namespace std;
int main() {
    int sum=0;
    string s,t,ans="";
    cin >> s;
    for (int i=0; i<s.length(); i++) {
        if (s[i] == ',') {
            sum += stoi(ans);
            ans = "";
        }
        else {
            ans += s[i];
        }
    }
    sum += stoi(ans);
    cout << sum << endl;
    return 0;
}