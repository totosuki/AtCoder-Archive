#include <bits/stdc++.h>
using namespace std;
int f(int x) { return x == 0 ? 1 : x * f(x - 1); }
int main() {
  int N;
  cin >> N;
  cout << f(N) << endl;
}