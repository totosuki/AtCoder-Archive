#include <bits/stdc++.h>
using namespace std;
int main() {
  int64_t N, K;
  cin >> N >> K;
  vector<int64_t> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  int64_t L = 0, R = 1e9;
  while (L < R) {
    int64_t M = (L + R) / 2;
    int64_t S = 0;
    for (int i = 0; i < N; i++) {
      S += M / A[i];
    }
    if (K <= S) {
      R = M;
    } else {
      L = M + 1;
    }
  }
  cout << L << endl;
}
