#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  cin >> A >> B;
  if (A % B == 0)
  {
    cout << 0 << endl;
  }
  else
  {
    cout << B - A % B << endl;
  }
}