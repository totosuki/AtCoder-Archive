#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, X;
  cin >> N >> X;
  cout << min(N - X, X - 1) << endl;
}