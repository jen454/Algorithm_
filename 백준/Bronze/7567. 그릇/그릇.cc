#include <iostream>
#include <string>
using namespace std;
int main() {
    string str;
    int cnt=10;
    cin >> str;
    for (int i=0; i<str.size()-1; i++) {
        if (str[i] != str[i+1]) cnt += 10;
        else cnt += 5;
    }
    cout << cnt << endl;
    return 0;
}