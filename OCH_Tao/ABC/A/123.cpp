#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> X(5);
  int K;
  for (int i = 0; i < 5; i++)
  {
    cin >> X[i];
  }
  cin >> K;
  bool flag = true;
  for (auto &i : X)
  {
    for (auto &j : X)
    {
      if (K < abs(i - j))
      {
        flag = false;
      }
    }
  }
  cout << (flag ? "Yay!" : ":(") << endl;
}