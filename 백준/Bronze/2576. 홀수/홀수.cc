#include <iostream>
using namespace std;
int main() {
    int N=7,num,min=100,sum=0,cnt=0;
    for (int i=0; i<N; i++) {
        cin >> num;
        if (num%2 != 0) {
            sum += num;
            if (num < min) {
                min = num;
            }
        }
        else {
            cnt++;
        }
        
    }
    if (cnt==N) cout << -1 << endl;
    else {
        cout << sum << endl;
        cout << min << endl;
    }
    return 0;
}