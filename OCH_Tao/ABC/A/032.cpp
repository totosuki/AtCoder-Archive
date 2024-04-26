#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, H;
  cin >> A >> B >> H;
  int i = H;
  bool flag = true;
  while (flag)
  {
    if (i % A == 0 && i % B == 0)
    {
      cout << i << endl;
      flag = false;
      break;
    }
    else
    {
      i++;
    }
  }
}