#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int N,num;
    cin >> N;
    vector<int> arr;
    for (int i=0; i<N; i++) {
        cin >> num;
        arr.push_back(num);
    }
    sort(arr.begin(), arr.end());
    arr.erase(unique(arr.begin(),arr.end()),arr.end());
    for (int i=0; i<arr.size(); i++) {
        cout << arr[i] << " ";
    }
    return 0;
}