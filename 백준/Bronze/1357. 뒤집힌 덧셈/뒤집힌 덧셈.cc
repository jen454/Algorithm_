#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    string x,y;
    cin >> x >> y;
    reverse(x.begin(),x.end());
    reverse(y.begin(),y.end());
    int X = stoi(x);
    int Y = stoi(y);
    int sum = X+Y;
    string s = to_string(sum);
    reverse(s.begin(),s.end());
    int res = stoi(s);
    cout << res << endl;
    return 0;
}