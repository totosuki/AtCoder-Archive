#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, K;
  cin >> N >> K;
  int cnt = 0;
  for (int i = 1; i < N + 1; i++) {
    for (int j = 1; j < N + 1; j++) {
      if (0 < K - (i + j) && K - (i + j) <= N) {
        cnt++;
      }
    }
  }
  cout << cnt << endl;
}