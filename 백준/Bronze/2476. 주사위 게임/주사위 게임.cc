#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n, arr[5] = {0}, mx = 0, score;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> arr[0] >> arr[1] >> arr[2];
        if(arr[0] == arr[1] and arr[1] == arr[2]){
            score = 10000 + arr[0] * 1000;
        } else if(arr[0] != arr[1] && arr[1] != arr[2] && arr[0] != arr[2]){
            score = *max_element(arr, arr+3) * 100;
        } else{
            sort(arr, arr+3);
            score = 1000 + arr[1] * 100;
        }
        if(mx < score) { mx = score; }
    }

    cout << mx << endl;
    
    return 0;
}