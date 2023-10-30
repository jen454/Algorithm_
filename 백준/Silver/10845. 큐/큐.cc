#include <iostream>
#include <queue>
#include <string>
using namespace std;
int main() {
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
                cout << q.front() << endl;
                q.pop();
            } else cout << -1 << endl;
        }
        else if (command == "size") {
            cout << q.size() << endl;
        }
        else if (command == "empty") {
            if (q.size() == 0) {
                cout << 1 << endl;
            } else cout << 0 << endl;
        }
        else if (command == "front") {
            if (q.size() != 0) {
                cout << q.front() << endl;
            } else cout << -1 << endl;
        }
        else if (command == "back") {
            if (q.size() != 0) {
                cout << q.back() << endl;
            } else cout << -1 << endl;
        }
    }
    return 0;
}