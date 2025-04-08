#include <bits/stdc++.h>
using namespace std;
int main()
{
  int X, Y;
  cin >> X >> Y;
  cout << (X >= Y ? 0 : ceil((double)(Y - X) / 10)) << endl;
}