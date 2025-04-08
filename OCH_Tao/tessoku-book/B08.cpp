#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  vector<vector<int>> L(1509, vector<int>(1509));
  for (int i = 0; i < N; i++) {
    int X, Y;
    cin >> X >> Y;
    L[X][Y]++;
  }
  for (int i = 1; i < 1501; i++) {
    for (int j = 1; j < 1501; j++) {
      L[i][j] += L[i][j - 1];
    }
  }
  for (int i = 1; i < 1501; i++) {
    for (int j = 1; j < 1501; j++) {
      L[j][i] += L[j - 1][i];
    }
  }
  int Q;
  cin >> Q;
  for (int i = 0; i < Q; i++) {
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    cout << L[C][D] + L[A - 1][B - 1] - L[A - 1][D] - L[C][B - 1] << endl;
  }
}