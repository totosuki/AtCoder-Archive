#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, K;
  string S;
  cin >> N >> K >> S;
  for (int i = 0; i < N; i++)
  {
    if (i == K - 1)
    {
      cout << char(S[i] + ('a' - 'A'));
    }
    else
    {
      cout << S[i];
    }
  }
  cout << endl;
}