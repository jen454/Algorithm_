#include <iostream>
#include <string>
using namespace std;
int main() {
    int cnt=0;
    string str;
    cin >> str;
    for (int i=0; i<str.size(); i++) {
        if (str[i] == ',') cnt++;
    }
    cout << cnt+1 << endl;
    return 0;
}