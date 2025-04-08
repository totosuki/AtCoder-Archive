#include <bits/stdc++.h>
using namespace std;
int main() {
  int A, B, C, X;
  cin >> A >> B >> C >> X;
  cout << fixed << setprecision(9);
  cout << (X <= A ? 1 : X <= B ? (double)C / double(B - A) : 0) << endl;
}