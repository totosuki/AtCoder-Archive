#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, K;
  cin >> N >> K;
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  vector<int64_t> B(N + 1);
  B[0] = 0;
  for (int i = 0; i < N; i++) {
    B[i + 1] = B[i] + A[i];
  }
  int64_t ans = 0;
  int R = 1;
  for (int i = 1; i < N + 1; i++) {
    while (R <= N && B[R] - B[i - 1] <= K) {
      R++;
    }
    ans += R - i;
  }
  cout << ans << endl;
}