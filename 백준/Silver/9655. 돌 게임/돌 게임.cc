#include <iostream>
using namespace std;
int main() {
    int N;
    cin >> N;
    if ((N-2)%2==0 || (N-4)%2==0 || (N-6)%2==0) cout << "CY" << endl;
    else cout << "SK" << endl;
    return 0;
}