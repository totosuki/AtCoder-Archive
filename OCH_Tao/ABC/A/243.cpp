#include <bits/stdc++.h>
using namespace std;
int main() {
  int V, A, B, C;
  cin >> V >> A >> B >> C;
  V %= A + B + C;
  cout << (V < A ? "F" : V < A + B ? "M" : "T") << endl;
}