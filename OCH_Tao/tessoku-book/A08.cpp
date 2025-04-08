#include <bits/stdc++.h>
using namespace std;
int main() {
  int H, W;
  cin >> H >> W;
  vector<vector<int>> X(H + 1, vector<int>(W + 1));
  for (int i = 1; i < H + 1; i++) {
    for (int j = 1; j < W + 1; j++) {
      cin >> X[i][j];
    }
  }
  for (int i = 1; i < H + 1; i++) {
    for (int j = 1; j < W + 1; j++) {
      X[i][j] += X[i][j - 1];
    }
  }
  for (int i = 1; i < W + 1; i++) {
    for (int j = 1; j < H + 1; j++) {
      X[j][i] += X[j - 1][i];
    }
  }
  int Q;
  cin >> Q;
  for (int i = 0; i < Q; i++) {
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    cout << X[C][D] + X[A - 1][B - 1] - X[A - 1][D] - X[C][B - 1] << endl;
  }
}