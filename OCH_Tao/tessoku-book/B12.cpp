#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  int L = 0, R = 50 * 1e6;
  while (L < R) {
    int M = (L + R) / 2;
    if (N <= pow((double)M / 1e6, 3) + (double)M / 1e6) {
      R = M;
    } else {
      L = M + 1;
    }
  }
  cout << fixed << setprecision(6) << (double)L / 1e6 << endl;
}