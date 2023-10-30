#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    string str;
    cin >> N;
    for (int i=0; i<N; i++) {
        string res ="";
        cin >> str;
        int n = str.length();
        for (int j=sqrt(n)-1; j>=0; j--) {
            for (int k=j; k<n; k+=sqrt(n)) {
                res += str[k];
            }
        }
        cout << res << "\n";
    }
    return 0;
}