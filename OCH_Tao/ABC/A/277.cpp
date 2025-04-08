#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, X;
  cin >> N >> X;
  vector<int> P(N);
  for (int i = 0; i < N; i++) {
    cin >> P[i];
  }
  cout << distance(P.begin(), find(P.begin(), P.end(), X)) + 1 << endl;
}