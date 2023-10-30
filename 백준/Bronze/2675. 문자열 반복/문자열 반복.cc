#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int n;
        string str;
        cin >> n;
        cin >> str;
        for (int j=0; j<str.size(); j++) {
            for (int k=0; k<n; k++) {
                cout << str[j];
            }
        }
        cout << "\n";
    }
    return 0;
}