#include <bits/stdc++.h>
using namespace std;
int main()
{
  int X, A, B;
  cin >> X >> A >> B;
  if (abs(X - A) < abs(X - B))
  {
    cout << "A" << endl;
  }
  else
  {
    cout << "B" << endl;
  }
}