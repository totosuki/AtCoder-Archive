#include <bits/stdc++.h>
using namespace std;
int main()
{
  set<int> S;
  for (int i = 0; i < 3; i++)
  {
    int x;
    cin >> x;
    S.insert(x);
  }
  cout << S.size() << endl;
}