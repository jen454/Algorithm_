#include <iostream>
using namespace std;
int main() {
    int T,N;
    cin >> T;
    for (int i=0; i<T; i++) {
        cin >> N;
        int num,sum=0;
        for (int j=0; j<N; j++) {
            cin >> num;
            sum += num;
        }
        cout << sum << endl;
    }
    return 0;
}