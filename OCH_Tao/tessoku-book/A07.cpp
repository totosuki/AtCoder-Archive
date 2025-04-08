#include <bits/stdc++.h>
using namespace std;
int main() {
  int D, N;
  cin >> D >> N;
  vector<int> X(D + 1);
  for (int i = 0; i < N; i++) {
    int L, R;
    cin >> L >> R;
    X[L - 1]++;
    X[R]--;
  }
  vector<int> ans(D + 1);
  ans[0] = 0;
  for (int i = 0; i < D; i++) {
    ans[i + 1] = ans[i] + X[i];
    cout << ans[i + 1] << endl;
  }
}