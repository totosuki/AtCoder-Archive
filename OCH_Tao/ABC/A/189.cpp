#include <bits/stdc++.h>
using namespace std;
int main()
{
  set<char> S;
  for (int i = 0; i < 3; i++)
  {
    char C;
    cin >> C;
    S.insert(C);
  }
  cout << (S.size() == 1 ? "Won" : "Lost") << endl;
}