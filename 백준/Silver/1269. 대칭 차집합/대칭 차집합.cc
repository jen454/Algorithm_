#include <iostream>
#include <set>
using namespace std;
int main() {
    int A,B,n;
    set<int> s;
    set<int>::iterator iter;
    cin >> A >> B;
    for (int i=0; i<A; i++) {
        cin >> n;
        s.insert(n);
    }
    for (int i=0; i<B; i++) {
        cin >> n;
        if (s.find(n) != s.end()) {
            s.erase(n);
        } else s.insert(n);
    }
    cout << s.size() << endl;
    return 0;
}