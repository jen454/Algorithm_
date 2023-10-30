#include <iostream>
using namespace std;
int main() {
    int x,y;
    cin >> x >> y;
    int sum=0;
    string arr[7] = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
    switch (x) {
        case 1:
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 2:
            sum += 31;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 3:
            sum += 59;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 4:
            sum += 90;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 5:
            sum += 120;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 6:
            sum += 151;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 7:
            sum += 181;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 8:
            sum += 212;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 9:
            sum += 243;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 10:
            sum += 273;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 11:
            sum += 304;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
        case 12:
            sum += 334;
            sum += y;
            cout << arr[sum%7] << endl;
            break;
    }
    return 0;
}