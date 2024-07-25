#include <bits/stdc++.h>
using namespace std;
int main()
{
  int cnt = 0;
  for (int i = 0; i < 4; i++)
  {
    char S;
    cin >> S;
    cnt += (S == '+' ? 1 : -1);
  }
  cout << cnt << endl;
}