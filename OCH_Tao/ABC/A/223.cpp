#include <bits/stdc++.h>
using namespace std;
int main()
{
  int X;
  cin >> X;
  cout << (X % 100 == 0 && X != 0 ? "Yes" : "No") << endl;
}