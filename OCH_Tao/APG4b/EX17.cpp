#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, S;
  cin >> N >> S;
  vector<int> A(N), P(N);
  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
  }
  for (int i = 0; i < N; i++) {
    cin >> P.at(i);
  }

  int cnt = 0;
  for (int X : A) {
    for (int Y : P) {
      if (X + Y == S) {
        cnt++;
      }
    }
  }
  cout << cnt << endl;
}
