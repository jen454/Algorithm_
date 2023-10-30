#include <iostream>
using namespace std;
int main() {
    int N;
    string str,res="",pre="";
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> str;
        if (res.length() == 0) {
            res = str;
        }
        else {
            for (int i=0; i<str.length(); i++) {
                if (res[i] != str[i]) res[i] = '?';
            }
        }    
    }
    cout << res << endl;
    return 0;
}