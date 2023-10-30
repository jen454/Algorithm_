#include <iostream>
#include <string>
using namespace std;
int main() {
    int T,N;
    cin >> T;
    for (int i=0; i<T; i++) {
        string str,ss="";
        cin >> N >> str;
        for (int j=0; j<str.size(); j++) {
            if (j+1 == N) continue;
            ss += str[j];
        }
        cout << ss << endl;
    }
    return 0;
}