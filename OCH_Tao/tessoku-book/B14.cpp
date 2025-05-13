#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, K;
  cin >> N >> K;
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  set<int> P, Q;
  int M = N / 2;
  for (int i = 1; i < (1 << M); i++) {
    int ans = 0;
    for (int j = 0; j < M; j++) {
      if ((i / (1 << j)) % 2 == 1) {
        ans += A[j];
      }
    }
    P.insert(ans);
  }
  for (int i = 1; i < (1 << (N - M)); i++) {
    int ans = 0;
    for (int j = 0; j < (N - M); j++) {
      if ((i / (1 << j)) % 2 == 1) {
        ans += A[M + j];
      }
    }
    Q.insert(ans);
  }
  if (P.count(K) || Q.count(K)) {
    cout << "Yes" << endl;
  } else {
    for (int i : P) {
      if (Q.count(K - i)) {
        cout << "Yes" << endl;
        return 0;
      }
    }
    cout << "No" << endl;
  }
}