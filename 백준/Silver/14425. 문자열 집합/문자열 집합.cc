#include <iostream>
#include <set>
using namespace std;
int main() {
    set<string> n;
    set<string>::iterator iter;
    int N,M,cnt=0;
    string s;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> s;
        n.insert(s);
    }
    for (int i=0; i<M; i++) {
        cin >> s;
        if (n.find(s) != n.end()) cnt++;
    }
    cout << cnt << endl;
    return 0;
}