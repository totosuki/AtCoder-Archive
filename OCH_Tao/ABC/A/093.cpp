#include <bits/stdc++.h>
using namespace std;
int main()
{
  char A, B, C;
  cin >> A >> B >> C;
  if (A != B && B != C && C != A)
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }
}