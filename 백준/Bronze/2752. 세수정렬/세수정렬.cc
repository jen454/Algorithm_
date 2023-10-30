#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    int arr[3] = {A,B,C};
    sort(arr,arr+3);
    cout << arr[0] << " " << arr[1] << " " << arr[2] << endl;
    return 0;
}