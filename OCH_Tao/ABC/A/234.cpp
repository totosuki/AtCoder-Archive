#include <bits/stdc++.h>
using namespace std;
int f(int x)
{
  return pow(x, 2) + 2 * x + 3;
}
int main()
{
  int T;
  cin >> T;
  cout << f(f(f(T) + T) + f(f(T))) << endl;
}