#include <iostream>
using namespace std;
int main() {
    int T,A,B,C,D,E,cnt=0;
    cin >>T>>A>>B>>C>>D>>E;
    if ((A%10) == T) {
        cnt++;
    }
    if ((B%10) == T) {
        cnt++;
    }
    if ((C%10) == T) {
        cnt++;
    }
    if ((D%10) == T) {
        cnt++;
    }
    if ((E%10) == T) {
        cnt++;
    }
    cout << cnt << endl;
    return 0;
}