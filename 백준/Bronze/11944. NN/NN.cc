#include <iostream>
#include <string>
using namespace std;
int main() {
    int N,M,cnt=0;
    cin >> N >> M;
    string str = to_string(N);
    string s = "";
    while (N) {
        s += str;
        cnt += str.length();
        if (cnt > M) {
            s.erase(M,s.length()-1);
            break;
        }
        if (cnt == M) break;
        N--;
    }
    cout << s << endl;
    return 0;
}