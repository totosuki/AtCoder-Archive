#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, Q;
  cin >> N;
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  sort(A.begin(), A.end());
  cin >> Q;
  for (int i = 0; i < Q; i++) {
    int X;
    cin >> X;
    int L = 0, R = N;
    while (L < R) {
      int M = (L + R) / 2;
      if (A[M] < X) {
        L = M + 1;
      } else {
        R = M;
      }
    }
    cout << L << endl;
  }
}