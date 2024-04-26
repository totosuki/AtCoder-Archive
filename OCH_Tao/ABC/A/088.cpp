#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, A;
  cin >> N >> A;
  for (int i = 0; i < A + 1; i++)
  {
    if ((N - i) % 500 == 0)
    {
      cout << "Yes" << endl;
      break;
    }
    if (i == A)
    {
      cout << "No" << endl;
    }
  }
}