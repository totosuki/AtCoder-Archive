#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cin >> N;
  vector<int> A(N);
  int sum = 0;
  for (int i = 0; i < N; i++)
  {
    int x;
    cin >> x;
    A.at(i) = x;
    sum += x;
  }
  sum /= N;
  for (int i = 0; i < N; i++)
  {
    int x = A.at(i);
    if (x < sum)
    {
      cout << sum - x << endl;
    }
    else if (x > sum)
    {
      cout << x - sum << endl;
    }
    else
    {
      cout << 0 << endl;
    }
  }
}