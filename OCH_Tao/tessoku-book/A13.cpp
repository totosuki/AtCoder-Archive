#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, K;
  vector<int> A(100009), R(100009);
  cin >> N >> K;
  for (int i = 1; i < N + 1; i++) {
    cin >> A[i];
  }
  int64_t ans = 0;
  for (int i = 1; i < N; i++) {
    if (i == 1) {
      R[i] = 1;
    } else {
      R[i] = R[i - 1];
    }
    while (R[i] < N && A[R[i] + 1] - A[i] <= K) {
      R[i]++;
    }
    ans += R[i] - i;
  }
  cout << ans << endl;
}