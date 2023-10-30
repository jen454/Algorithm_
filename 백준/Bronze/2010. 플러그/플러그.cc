#include <iostream>
using namespace std;
int main() {
    int N;
    int n,sum=0;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> n;
        sum += n;
    }
    cout << sum-(N-1) << endl;
    return 0;
}