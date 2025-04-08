#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, X;
  cin >> N >> X;
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  int L = 0;
  int R = N - 1;
  while (L <= R) {
    int M = (L + R) / 2;
    if (X == A[M]) {
      cout << M + 1 << endl;
      break;
    }
    if (X < A[M]) {
      R = M - 1;
    }
    if (X > A[M]) {
      L = M + 1;
    }
  }
}