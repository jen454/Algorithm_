#include <iostream>
using namespace std;
int main() {
    int i;
    long long S,sum;
    cin >> S;
    sum = 0;
    i = 0;
    while (sum <= S) {
        i++;
        sum += i;
    }
    cout << i-1 << endl;
    return 0;
}