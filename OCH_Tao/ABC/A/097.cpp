#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C, D;
  cin >> A >> B >> C >> D;
  if (abs(A - C) <= D || (abs(A - B) <= D && abs(B - C) <= D))
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }
}