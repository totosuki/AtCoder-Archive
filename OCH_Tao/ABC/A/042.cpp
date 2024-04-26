#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> X(3);
  for (int i = 0; i < 3; i++)
  {
    cin >> X[i];
  }
  int five, seven;
  five = count(X.begin(), X.end(), 5);
  seven = count(X.begin(), X.end(), 7);
  if (five == 2 && seven == 1)
  {
    cout << "YES" << endl;
  }
  else
  {
    cout << "NO" << endl;
  }
}