#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, A, X, Y;
  cin >> N >> A >> X >> Y;
  cout << min(N, A) * X + max(0, N - A) * Y << endl;
}