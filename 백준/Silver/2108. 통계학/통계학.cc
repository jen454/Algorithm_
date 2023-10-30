#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int N;
int num[500001];
int arithmetic_mean(){
    double ans = 0;
    for (int i=0; i<N; i++){
        ans += num[i];
    }
    return round(ans / N);
} //산술평균
int medain(){
    return num[N/2];
} //중앙값
int mode(){
    int result;
    int count = 0;
    int cnt2[8001] = {0};
    for (int i=0; i<N; i++){
        cnt2[num[i] + 4000]++;
    }
    int max_mode = *max_element(cnt2, cnt2 + 8001);
    for (int i=0; i<8001; i++){
        if(cnt2[i] == max_mode){
            count++;
            result = i - 4000;
        }
        if(count == 2){
            break;
        }
    }
    return result;
}//최빈값
int range(){
    return num[N-1] - num[0];
}//범위
int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> num[i];
    }
    sort(num, num + N);
    cout << arithmetic_mean() << endl;
    cout << medain() << endl;
    cout << mode() << endl;
    cout << range() << endl;
    return 0;
}