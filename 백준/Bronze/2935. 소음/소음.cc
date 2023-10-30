#include <iostream>
#include <string>
using namespace std;
 
int main() {
    string A, B, result, temp;
    char op;
    cin >> A >> op >> B;
    
    int aLen = A.length(), bLen = B.length();
    if (op == '*') {
        result = "1";
        for(int i=0; i< aLen-1 + bLen-1; i++){
            result += '0';
        }
        cout << result << endl;
        return 0;
    }
 
    if(aLen == bLen){
        result = A;
        result[0] = '2';
    }
    else{
        if(aLen < bLen){
            temp = A;
            A = B;
            B = temp;
        }
        result = A;
        result[A.length() - B.length()] = '1';
    }
    cout << result << endl;
}