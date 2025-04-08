#include <bits/stdc++.h>
using namespace std;
int main() {
  int T, N;
  cin >> T >> N;
  vector<int> X(T);
  for (int i = 0; i < N; i++) {
    int L, R;
    cin >> L >> R;
    X[L]++;
    X[R]--;
  }
  vector<int> ans(T);
  for (int i = 0; i < T; i++) {
    ans[i + 1] = ans[i] + X[i];
    cout << ans[i + 1] << endl;
  }
}