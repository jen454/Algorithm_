#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int A,B,C;
    cin >> A >> B >> C;
    int Array[3] = {A,B,C};
    sort(Array, Array+3);
    cout << Array[1] << endl;
    return 0;
}
