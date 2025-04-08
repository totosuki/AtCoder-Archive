#include <bits/stdc++.h>
using namespace std;
int main() {
  int H, W;
  cin >> H >> W;
  int cnt = 0;
  for (int i = 0; i < H; i++) {
    string S;
    cin >> S;
    for (char j : S) {
      if (j == '#') {
        cnt++;
      }
    }
  }
  cout << cnt << endl;
}