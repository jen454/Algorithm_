#include <iostream>
#include <string>
using namespace std;
int main() {
    int T;
    string str;
    cin >> T;
    for (int i=0; i<T; i++) {
        cin >> str;
        int sum=0,cnt=0;
        for (int j=0; j<str.size(); j++) {
            if (str[j] == 'O') {
                cnt++;
                sum += cnt;
            }
            else cnt = 0;
        }
        cout << sum << endl;
    }
    return 0;
}