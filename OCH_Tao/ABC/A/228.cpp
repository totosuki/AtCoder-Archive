#include <bits/stdc++.h>
using namespace std;
int main()
{
  int S, T, X;
  cin >> S >> T >> X;
  if (S < T)
  {
    cout << (S <= X && X < T ? "Yes" : "No") << endl;
  }
  else
  {
    cout << (X < T || S <= X ? "Yes" : "No") << endl;
  }
}