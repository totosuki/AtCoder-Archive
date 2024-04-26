#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, K, X, Y;
  cin >> N >> K >> X >> Y;
  int cnt = 0;
  for (int i = 1; i < N + 1; i++)
  {
    if (i <= K)
    {
      cnt += X;
    }
    else
    {
      cnt += Y;
    }
  }
  cout << cnt << endl;
}