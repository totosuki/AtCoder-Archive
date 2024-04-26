#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cin >> N;
  bitset<4> X(N);
  cout << X.count() << endl;
  string A = X.to_string();
  reverse(A.begin(), A.end());
  for (int i = 0; i < 4; i++)
  {
    if (A[i] == '1')
    {
      cout << pow(2, i) << endl;
    }
  }
}