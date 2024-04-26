#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C, cnt;
  cin >> A >> B >> C;
  cnt = 0;
  while (C >= min(A, B))
  {
    cnt++;
    C -= min(A, B);
  }
  cout << cnt << endl;
}