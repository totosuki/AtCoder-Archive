#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> L(3);
  for (int i = 0; i < 3; i++)
  {
    cin >> L[i];
  }
  sort(L.begin(), L.end());
  cout << L[0] + L[1] << endl;
}