#include <iostream>
#include <map>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N,M;
    map<string,string> m;
    string a,b;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> a >> b;
        m.insert({a,b});
    }
    while (M) {
        cin >> a;
        cout << m[a] << "\n";
        M--;
    }
    return 0;
}