#include <iostream>
#include <map>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);  
    map<string,int> m;
    map<string,int>::iterator iter;
    int N;
    cin >> N;
    string s;
    for (int i=0; i<N; i++) {
        cin >> s;
        if (m.find(s) == m.end()) {
            m.insert({s,1});
        } else m[s]++;
    }
    int max = 0;
    string max_s;
    for (auto iter:m) {
        if (iter.second > max) {
            max_s = iter.first;
            max = iter.second;
        }
    }
    cout << max_s << "\n";
    return 0;
}