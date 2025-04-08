#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, Q;
  cin >> N >> Q;
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  vector<int> X(N + 1);
  X[0] = 0;
  for (int i = 0; i < N; i++) {
    X[i + 1] = X[i] + A[i];
  }
  for (int i = 0; i < Q; i++) {
    int L, R;
    cin >> L >> R;
    cout << X[R] - X[L - 1] << endl;
  }
}