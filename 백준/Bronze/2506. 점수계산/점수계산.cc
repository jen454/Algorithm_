#include <iostream>
using namespace std;
int main() {
    int N,num,sum=0,cnt=0;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> num;
        if (num == 1) {
            sum += 1;
        }
        else {
            sum = 0;
        }
        cnt += sum;
    }
    cout << cnt << endl;
    return 0;
}