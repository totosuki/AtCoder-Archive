#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  vector<int> P(100009), Q(100009);
  for (int i = 1; i < N + 1; i++) {
    P[i] = max(P[i - 1], A[i - 1]);
  }
  for (int i = 1; i < N + 1; i++) {
    Q[i] = max(Q[i - 1], A[N - i]);
  }
  int D;
  cin >> D;
  for (int i = 0; i < D; i++) {
    int L, R;
    cin >> L >> R;
    cout << max(P[L - 1], Q[N - R]) << endl;
  }
}