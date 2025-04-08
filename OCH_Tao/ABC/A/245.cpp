#include <bits/stdc++.h>
using namespace std;
int main() {
  int A, B, C, D;
  cin >> A >> B >> C >> D;
  cout << (A * 60 + B <= C * 60 + D ? "Takahashi" : "Aoki") << endl;
}