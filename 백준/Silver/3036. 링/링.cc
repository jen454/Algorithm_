#include <iostream>
using namespace std;
int gcd(int a, int b)
{ 
	if (a % b == 0) 
    	return b;
	else
    	return gcd(b, a % b);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    cin >> N;
    int arr[N];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }
    for (int i=1; i<N; i++) {
        int base = gcd(arr[0],arr[i]);
        cout << arr[0]/base << "/" << arr[i]/base << endl;
    }
    return 0;
}