#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for (int i=0; i<my_string.length(); i++) {
        if (my_string[i] >= 'a' && my_string[i] <= 'z') {
            my_string[i] -= 32;
            answer += my_string[i];
        } else {
            my_string[i] += 32;
            answer += my_string[i];
        }
    }
    return answer;
}