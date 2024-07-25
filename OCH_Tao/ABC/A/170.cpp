#include <bits/stdc++.h>
using namespace std;
int main()
{
  int cnt = 0;
  for (int i = 0; i < 5; i++)
  {
    int X;
    cin >> X;
    cnt += X;
  }
  cout << 15 - cnt << endl;
}