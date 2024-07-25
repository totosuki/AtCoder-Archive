#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, R;
  cin >> N >> R;
  cout << R + max(0, 10 - N) * 100 << endl;
}