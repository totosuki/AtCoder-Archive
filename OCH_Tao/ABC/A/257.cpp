#include <bits/stdc++.h>
using namespace std;
int main() {
  string S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  double N, X;
  cin >> N >> X;
  cout << S[ceil(X / N) - 1] << endl;
}