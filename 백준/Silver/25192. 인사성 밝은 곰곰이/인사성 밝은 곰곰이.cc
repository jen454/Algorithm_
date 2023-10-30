#include <iostream>
#include <set>
using namespace std;
int main() {
    int N,cnt=0;
    string str;
    set<string> s;
    set<string>::iterator iter;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> str;
        if (str == "ENTER") {
            s.clear();
        }
        else {
            if (s.find(str) == s.end()) cnt++;
            s.insert(str);
        }
    }
    cout << cnt << endl;
    return 0;
}