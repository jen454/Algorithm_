#include <iostream>
#include <string>
using namespace std;
int main() {
    int N;
    string s;
    cin >> N;
    cin.ignore();
    for (int i=0; i<N; i++) {
        getline(cin,s);
        if ('a' <= s[0] && s[0] <= 'z') {
            s[0] -= 32;
        }
        cout << s << endl;
    }
    return 0;
}