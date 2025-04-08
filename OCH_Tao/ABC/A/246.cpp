#include <bits/stdc++.h>
using namespace std;
int main() {
  int X1, X2, X3, Y1, Y2, Y3;
  cin >> X1 >> Y1 >> X2 >> Y2 >> X3 >> Y3;
  cout << (X1 ^ X2 ^ X3) << ' ' << (Y1 ^ Y2 ^ Y3) << endl;
}