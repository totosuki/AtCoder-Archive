#include <bits/stdc++.h>
using namespace std;
int main() {
  int R, C;
  cin >> R >> C;
  vector<int> A1(2);
  vector<int> A2(2);
  for (int i = 0; i < 2; i++) {
    cin >> A1[i];
  }
  for (int i = 0; i < 2; i++) {
    cin >> A2[i];
  }
  cout << (R == 1 ? A1[C - 1] : A2[C - 1]) << endl;
}