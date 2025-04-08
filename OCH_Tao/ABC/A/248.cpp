#include <bits/stdc++.h>
using namespace std;
int main() {
  int cnt = 0;
  for (int i = 0; i < 9; i++) {
    char S;
    cin >> S;
    cnt += S - '0';
  }
  cout << 45 - cnt << endl;
}