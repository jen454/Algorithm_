#include <iostream>
#include <map>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    map<string,int> m;
    map<string,int>::iterator iter;
    int T,n;
    cin >> T;
    string cloth,name;
    for (int i=0; i<T; i++) {
        int res = 1;
        cin >> n;
        m.clear();
        for (int i=0; i<n; i++) {
            cin >> cloth >> name;
            if (m.find(name) == m.end()) {
                m.insert({name,1});
            } else m[name]++;
        }
        for (auto iter = m.begin(); iter !=  m.end(); iter++) {
	        res *= (iter->second)+1;
        }
        cout << res-1 << endl;
    }
    return 0;
}