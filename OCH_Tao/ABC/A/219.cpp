#include <bits/stdc++.h>
using namespace std;
int main()
{
  int X;
  cin >> X;
  if (90 <= X)
  {
    cout << "expert";
  }
  else if (70 <= X)
  {
    cout << 90 - X;
  }
  else if (40 <= X)
  {
    cout << 70 - X;
  }
  else
  {
    cout << 40 - X;
  }
  cout << endl;
}