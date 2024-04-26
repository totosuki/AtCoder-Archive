#include <bits/stdc++.h>
using namespace std;
int main()
{
  int L1, L2, L3;
  cin >> L1 >> L2 >> L3;
  if (L1 == L2)
  {
    cout << L3 << endl;
  }
  else if (L2 == L3)
  {
    cout << L1 << endl;
  }
  else
  {
    cout << L2 << endl;
  }
}