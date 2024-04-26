#include <bits/stdc++.h>
using namespace std;
int main()
{
  for (int i = 0; i < 19; i++)
  {
    char x;
    cin >> x;
    if (i == 5 || i == 13)
    {
      cout << ' ';
    }
    else
    {
      cout << x;
    }
  }
  cout << endl;
}