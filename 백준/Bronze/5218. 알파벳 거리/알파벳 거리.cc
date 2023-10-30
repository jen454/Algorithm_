#include <iostream>
#include <string>
using namespace std;
int main() {
    int T;
    string a, b;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> a >> b;
        int *arr = new int[a.size()];
        for (int i = 0; i < a.size(); i++)
        {
            if (b[i] >= a[i])
                arr[i] = b[i] - a[i];
            else if (b[i] < a[i])
                arr[i] = b[i] + 26 - a[i];
        }
        cout << "Distances: ";
        for (int i = 0; i < a.size(); i++)
        {
            cout  << arr[i]<<' ';
        }
        cout << '\n';
    }
    return 0;
}