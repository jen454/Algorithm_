#include <iostream>
using namespace std;

int Fibo(int N) {
    if (N==0) return 0;
    if (N==1 || N==2) return 1;
    return Fibo(N-1) + Fibo(N-2);
}

int main() {
    int n;
    cin >> n;
    cout << Fibo(n) << endl;
    return 0;
}