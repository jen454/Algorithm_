#include <iostream>
using namespace std;
int main() {
    int N,A=0,B=0,n;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> n;
        if (n==1) A++;
        else B++;
    }
    if (A>B) cout << "Junhee is cute!" << endl;
    else cout << "Junhee is not cute!" << endl;
}