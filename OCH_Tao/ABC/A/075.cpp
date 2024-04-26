#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C;
  cin >> A >> B >> C;
  if (B == C)
  {
    cout << A;
  }
  else if (C == A)
  {
    cout << B;
  }
  else
  {
    cout << C;
  }
  cout << endl;
}