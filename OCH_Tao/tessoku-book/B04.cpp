#include <bits/stdc++.h>
using namespace std;
int main() {
  string N;
  cin >> N;
  reverse(N.begin(), N.end());
  int cnt = 0;
  for (int i = 0; i < N.size(); i++) {
    if (N[i] == '1') {
      cnt += pow(2, i);
    }
  }
  cout << cnt << endl;
}