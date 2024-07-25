#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> L(3);
  for (int i = 0; i < 3; i++)
  {
    cin >> L[i];
  }
  cout << reduce(L.begin(), L.end()) - *max_element(L.begin(), L.end()) << endl;
}