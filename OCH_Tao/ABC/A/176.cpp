#include <bits/stdc++.h>
using namespace std;
int main()
{
  float N, X;
  int T;
  cin >> N >> X >> T;
  cout << (int)ceil(N / X) * T << endl;
}