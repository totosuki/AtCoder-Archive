#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cin >> N;
  int X = 0;
  for (int i = 1; i < N + 1; i++)
  {
    X += i * 10000;
  }
  cout << X / N << endl;
}