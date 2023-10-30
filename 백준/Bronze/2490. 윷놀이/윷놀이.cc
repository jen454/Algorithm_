#include <iostream>
using namespace std;
int main() {
    int A,B,C,D;
    for (int i=0; i<3; i++) {
        cin >>A>>B>>C>>D;
        switch (A+B+C+D) {
            case 0:
                cout << "D" << endl;
                break;
            case 1:
                cout << "C" << endl;
                break;
            case 2:
                cout << "B" << endl;
                break;
            case 3:
                cout << "A" << endl;
                break;
            case 4:
                cout << "E" << endl;
                break;
        }
    }
    return 0;
   
}