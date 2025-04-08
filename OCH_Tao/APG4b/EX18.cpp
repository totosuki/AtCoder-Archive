#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<vector<char>> ans(N, vector<char>(N, '-'));
  for (int i = 0; i < M; i++) {
    int A, B;
    cin >> A >> B;
    ans[A - 1][B - 1] = 'o';
    ans[B - 1][A - 1] = 'x';
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cout << ans[i][j];
      if (j < N - 1) {
        cout << ' ';
      }
    }
    cout << endl;
  }
}
