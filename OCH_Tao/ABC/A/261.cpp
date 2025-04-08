#include <bits/stdc++.h>
using namespace std;
int main() {
  int L1, R1, L2, R2;
  cin >> L1 >> R1 >> L2 >> R2;
  cout << max(0, min(R1, R2) - max(L1, L2)) << endl;
}