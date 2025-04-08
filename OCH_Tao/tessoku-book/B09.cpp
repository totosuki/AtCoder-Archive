#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  vector<vector<int>> X(1509, vector<int>(1509));
  for (int i = 0; i < N; i++) {
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    X[A + 1][B + 1]++;
    X[C + 1][D + 1]++;
    X[A + 1][D + 1]--;
    X[C + 1][B + 1]--;
  }
  for (int i = 1; i < 1509; i++) {
    for (int j = 1; j < 1509; j++) {
      X[i][j] += X[i][j - 1];
    }
  }
  for (int i = 1; i < 1509; i++) {
    for (int j = 1; j < 1509; j++) {
      X[j][i] += X[j - 1][i];
    }
  }
  int cnt = 0;
  for (auto i : X) {
    for (auto j : i) {
      if (j > 0) {
        cnt++;
      }
    }
  }
  cout << cnt << endl;
}