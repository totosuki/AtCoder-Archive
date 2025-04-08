#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, M, X, T, D;
  cin >> N >> M >> X >> T >> D;
  cout << (X <= M ? T : T - D * (X - M)) << endl;
}