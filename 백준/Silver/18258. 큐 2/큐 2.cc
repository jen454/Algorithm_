#include <iostream>
#include <queue>
#include <string>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    queue<int> q;
    int N;
    string command;
    int command_num;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> command;
        if (command == "push") {
            cin >> command_num;
            q.push(command_num);
        }
        else if (command == "pop") {
            if (q.size() != 0) {
                cout << q.front() << "\n";
                q.pop();
            } else cout << -1 << "\n";
        }
        else if (command == "size") {
            cout << q.size() << "\n";
        }
        else if (command == "empty") {
            if (q.size() == 0) {
                cout << 1 << "\n";
            } else cout << 0 << "\n";
        }
        else if (command == "front") {
            if (q.size() != 0) {
                cout << q.front() << "\n";
            } else cout << -1 << "\n";
        }
        else if (command == "back") {
            if (q.size() != 0) {
                cout << q.back() << "\n";
            } else cout << -1 << "\n";
        }
    }
    return 0;
}