#include <bits/stdc++.h>
using namespace std;
int main()
{
  set<int> A = {1, 3, 5, 7, 8, 10, 12};
  set<int> B = {4, 6, 9, 11};
  set<int> C = {2};
  int X, Y;
  cin >> X >> Y;
  if (A.count(X) && A.count(Y))
  {
    cout << "Yes";
  }
  else if (B.count(X) && B.count(Y))
  {
    cout << "Yes";
  }
  else if (C.count(X) && C.count(Y))
  {
    cout << "Yes";
  }
  else
  {
    cout << "No";
  }
  cout << endl;
}