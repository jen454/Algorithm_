#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	while (true) {
        ios::sync_with_stdio(false);
        cin.tie(NULL); cout.tie(NULL);
		string input;
		getline(cin,input);
        if (input[0] == '.') break; 
		stack<char> st;
        bool flag = 0;
		for (int i = 0; i < input.length(); i++) {
			if (input[i] == '(' || input[i] == '[') {
				st.push(input[i]);
			}
			else if (input[i] == ')') {
                if (!st.empty() && st.top() == '(') st.pop();
                else {
                    flag = 1;
                    break;
                }
			}
            else if (input[i] == ']') {
                if (!st.empty() && st.top() == '[') st.pop();
                else {
                    flag = 1;
                    break;
                }
			}
		}
        if (flag == 0 && st.empty()) {
            cout << "yes" << endl;
        } else {
            cout << "no" << endl;
        }
	}
	return 0;
}