#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n,num;
    cin >> n;
    for (int i=0; i<n; i++) {
        int cnt = 0;
        cin >> num;
        bool arr[101] = {true,};
        for (int j=2; j<=num; j++) {
            for (int k=j; k<=num; k+=j) {
                if (arr[k] == true) arr[k] = false;
                else arr[k] = true;
            }
        }
        for (int j=1; j<=num; j++) {
            if (arr[j] == true) cnt++;
        }
        cout << num-cnt << "\n";
    }
    return 0;
}