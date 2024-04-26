#include <bits/stdc++.h>
using namespace std;
int main()
{
  string C1, C2;
  cin >> C1 >> C2;
  reverse(C2.begin(), C2.end());
  if (C1 == C2)
  {
    cout << "YES" << endl;
  }
  else
  {
    cout << "NO" << endl;
  }
}