#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    int arr[100000];
    int time[1000000];
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }
    sort(arr,arr+N,greater<int>());
    for (int i=0; i<N; i++) {
        time[i] = (i+1) + arr[i];
    }
    sort(time,time+N,greater<int>());
    cout << time[0]+1 << "\n";
    return 0;
}