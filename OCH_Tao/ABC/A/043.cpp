#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cin >> N;
  int cnt = 0;
  for (int i = 1; i < N + 1; i++)
  {
    cnt += i;
  }
  cout << cnt << endl;
}