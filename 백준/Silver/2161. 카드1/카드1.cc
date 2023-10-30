#include <iostream>
#include <deque>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);  
    deque<int> dq;
    deque<int>::iterator iter;
    bool ans = true;
    int N;
    cin >> N;
    for (int i=1; i<=N; i++) {
        dq.push_back(i);
    }
    while (N) {
        if (ans==true) {
            cout << dq.front() << " ";
            dq.pop_front();
            N--;
            ans = false;
        }
        else {
            dq.push_back(dq.front());
            dq.pop_front();
            ans = true;
        }
    }
    return 0;
}