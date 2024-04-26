#include <bits/stdc++.h>
using namespace std;
int main()
{
  string A = "ABCDE";
  char X;
  cin >> X;
  for (int i = 0; i < 5; i++)
  {
    if (A.at(i) == X)
    {
      cout << i + 1 << endl;
    }
  }
}