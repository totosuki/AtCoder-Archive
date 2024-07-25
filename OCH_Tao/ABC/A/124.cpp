#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  int cnt = 0;
  cin >> A >> B;
  for (int i = 0; i < 2; i++)
  {
    if (A > B)
    {
      cnt += A;
      A--;
    }
    else
    {
      cnt += B;
      B--;
    }
  }
  cout << cnt << endl;
}