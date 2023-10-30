#include <iostream>
#include <set>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int A,B,n;
    set<int> s;
    set<int>::iterator iter;
    cin >> A >> B;
    for (int i=0; i<A; i++) {
        cin >> n;
        s.insert(n);
    }
    int cnt = s.size();
    for (int i=0; i<B; i++) {
        cin >> n;
        if (s.find(n) != s.end()) {
            s.erase(n);
        }
    }
    cout << s.size() << "\n";
	for (iter = s.begin(); iter != s.end(); iter++) {
		cout << *iter << " ";
	}
	cout << "\n";
    return 0;
}