#include <bits/stdc++.h>
using namespace std;
int main() {
  int H, W, N;
  cin >> H >> W >> N;
  vector<vector<int>> X(H + 9, vector<int>(W + 9));
  for (int i = 0; i < N; i++) {
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    X[A][B]++;
    X[C + 1][D + 1]++;
    X[A][D + 1]--;
    X[C + 1][B]--;
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
  for (int i = 1; i < H + 1; i++) {
    for (int j = 1; j < W + 1; j++) {
      cout << X[i][j];
      if (j < W) {
        cout << " ";
      }
    }
    cout << endl;
  }
}