#include <bits/stdc++.h>
using namespace std;
int main() {
  string S;
  cin >> S;
  int cnt = 0;
  for (char x : S) {
    if (x == 'w') {
      cnt += 2;
    } else {
      cnt++;
    }
  }
  cout << cnt << endl;
}