#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    string s;
    cin >> s;
    string arr[s.length()];
    for (int i=0; i<s.length(); i++) {
        arr[i] = s.substr(i,s.length());
    }
    sort(arr,arr+s.length());
    for (string str:arr) {
        cout << str << endl;
    }
    return 0;
}