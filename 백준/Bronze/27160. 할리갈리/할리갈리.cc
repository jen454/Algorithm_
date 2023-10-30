#include <iostream>
#include <map>
using namespace std;
int main() {
    int N,X;
    string card,ans="NO";
    map<string,int> m;
    map<string,int>::iterator iter;
    cin >> N;
    m.insert({"STRAWBERRY",0});
    m.insert({"BANANA",0});
    m.insert({"LIME",0});
    m.insert({"PLUM",0});
    for (int i=0; i<N; i++) {
        cin >> card >> X;
        m[card] += X;
    }
    for (auto iter:m) {
        if (iter.second == 5) {
            ans = "YES";
            break;
        } 
    }
    cout << ans << "\n";
    return 0;
}