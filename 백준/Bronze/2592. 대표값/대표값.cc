#include <iostream>

using namespace std;

int main()
{
  int sum = 0, arr[1001] = {0,}, checker = 0, ans;

  for (int i = 0; i < 10; i++) {
    int tmp;
    cin >> tmp;

    arr[tmp]++;
    sum += tmp;
  }

  for (int i = 10; i < 1001; i+=10) {
    if(arr[i] && checker < arr[i]) {
      checker = arr[i];
      ans = i;
    }
  }

  cout << sum/10 << endl;
  cout << ans << endl;
  return 0;
}