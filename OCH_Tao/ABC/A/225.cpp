#include <bits/stdc++.h>
using namespace std;
int main()
{
  set<char> S;
  for (int i = 0; i < 3; i++)
  {
    char X;
    cin >> X;
    S.insert(X);
  }
  if (S.size() == 1)
  {
    cout << 1 << endl;
  }
  else if (S.size() == 2)
  {
    cout << 3 << endl;
  }
  else
  {
    cout << 6 << endl;
  }
}