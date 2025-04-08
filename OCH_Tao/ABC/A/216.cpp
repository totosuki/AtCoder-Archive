#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  string X = S.substr(0, S.size() - 2);
  int Y = S[S.size() - 1] - '0';
  if (Y < 3)
  {
    cout << X << "-" << endl;
  }
  else if (Y < 7)
  {
    cout << X << endl;
  }
  else
  {
    cout << X << "+" << endl;
  }
}