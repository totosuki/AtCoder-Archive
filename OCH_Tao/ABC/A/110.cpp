#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> X(3);
  for (int i = 0; i < 3; i++)
  {
    cin >> X[i];
  }
  int sum = reduce(X.begin(), X.end(), 0);
  int MX = *max_element(X.begin(), X.end());
  cout << sum + MX * 10 - MX << endl;
}