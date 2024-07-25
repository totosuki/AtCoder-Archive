#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  if (S.find("RRR") != string::npos)
  {
    cout << 3 << endl;
  }
  else if (S.find("RR") != string::npos)
  {
    cout << 2 << endl;
  }
  else if (S.find("R") != string::npos)
  {
    cout << 1 << endl;
  }
  else
  {
    cout << 0 << endl;
  }
}