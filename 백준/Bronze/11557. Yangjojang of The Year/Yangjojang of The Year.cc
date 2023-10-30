#include <iostream>
#include <string>
using namespace std;
int main() {
    int T,N,max=-1,num;
    string uni,name="";
    cin >> T;
    for (int i=0; i<T; i++) {
        cin >> N;
        for (int j=0; j<N; j++) {
            cin >> uni >> num;
            if (num > max) {
                name = uni;
                max = num;
            }
        }
        cout << name << endl;
    }
    return 0;
}