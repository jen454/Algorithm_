#include <iostream>
using namespace std;
int main() {
    int arr[26] = {0,};
    string s;
    cin >> s;
    for (int i=0; i<s.length(); i++) {
        arr[s[i]-'a']++;
    }
    for (int i:arr) {
        cout << i << " ";
    }
    return 0;
}