#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  int N = S.size();
  int x = 1;
  for (int i = 1; i < N; i++)
  {
    if (S.at(i) == '+')
    {
      x++;
    }
    else if (S.at(i) == '-')
    {
      x--;
    }
    else
    {
      continue;
    }
  }
  cout << x << endl;
}