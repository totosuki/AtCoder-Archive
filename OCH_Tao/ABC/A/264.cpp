#include <bits/stdc++.h>
using namespace std;
int main() {
  int L, R;
  string S = "atcoder";
  cin >> L >> R;
  cout << S.substr(L - 1, R - L + 1) << endl;
}