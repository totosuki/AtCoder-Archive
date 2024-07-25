#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  if (S.back() == 's')
  {
    cout << S << "es" << endl;
  }
  else
  {
    cout << S << "s" << endl;
  }
}