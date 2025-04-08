#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  int ans = 0;
  int tmp = 0;
  for (int i = 0; i < N; i++) {
    int H;
    cin >> H;
    if (tmp < H) {
      ans = i;
      tmp = H;
    }
  }
  cout << ans + 1 << endl;
}