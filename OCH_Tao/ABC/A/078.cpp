#include <bits/stdc++.h>
using namespace std;
int main()
{
  string X, Y;
  cin >> X >> Y;
  if (X < Y)
  {
    cout << "<" << endl;
  }
  else if (X > Y)
  {
    cout << ">" << endl;
  }
  else
  {
    cout << "=" << endl;
  }
}