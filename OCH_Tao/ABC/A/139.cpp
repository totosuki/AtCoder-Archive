#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S, T;
  cin >> S >> T;
  int cnt = 0;
  for (int i = 0; i < 3; i++)
  {
    if (S[i] == T[i])
    {
      cnt++;
    }
  }
  cout << cnt << endl;
}