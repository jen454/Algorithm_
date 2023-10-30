#include <iostream>
using namespace std;
int main() {
    int N,A=0,B=0;
    char chr;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> chr;
        if (chr == 'A') {
            A++;
        } else B++;
    }
    if (A > B) cout << "A" << endl;
    else if (A < B) cout << "B" << endl;
    else cout << "Tie" << endl;
    return 0;
}
