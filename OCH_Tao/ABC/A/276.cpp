#include <bits/stdc++.h>
using namespace std;
int main() {
  string S;
  cin >> S;
  int ans = -1;
  for (int i = S.size(); i > 0; i--) {
    if (S[i - 1] == 'a') {
      ans = i;
      break;
    }
  }
  cout << ans << endl;
}