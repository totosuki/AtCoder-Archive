#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C, K, S, T;
  cin >> A >> B >> C >> K >> S >> T;
  if (S + T < K)
  {
    cout << A * S + B * T << endl;
  }
  else
  {
    cout << A * S + B * T - C * (S + T) << endl;
  }
}