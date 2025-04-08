#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, Q;
  cin >> N;
  vector<int> A(N), X(N + 1);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  X[0] = 0;
  for (int i = 0; i < N; i++) {
    X[i + 1] = X[i] + A[i];
  }
  cin >> Q;
  for (int i = 0; i < Q; i++) {
    int L, R, ans;
    cin >> L >> R;
    ans = X[R] - X[L - 1];
    cout << (ans > (R - L + 1) - ans ? "win" : ans < (R - L + 1) - ans ? "lose" : "draw") << endl;
  }
}