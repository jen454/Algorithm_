#include <iostream>
#include <set>
using namespace std;

int main() {
    int N,cnt=0;
    string name,game;
    cin >> N >> game;
    set<string> s;
    set<string>::iterator iter;
    for (int i=0; i<N; i++) {
        cin >> name;
        s.insert(name);
    }
    if (game == "Y") cnt += s.size();
    else if (game == "F") cnt += (s.size()/2);
    else cnt += (s.size()/3);
    cout << cnt << endl;
    return 0;
}