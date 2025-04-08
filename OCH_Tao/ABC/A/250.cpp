#include <bits/stdc++.h>
using namespace std;
int main() {
  int H, W, R, C;
  cin >> H >> W >> R >> C;
  int cnt = 0;
  if (R != 1) {
    cnt++;
  }
  if (R != H) {
    cnt++;
  }
  if (C != 1) {
    cnt++;
  }
  if (C != W) {
    cnt++;
  }
  cout << cnt << endl;
}