#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  int N;
  cin >> S >> N;
  cout << S[(N - 1) / 5] << S[(N - 1) % 5] << endl;
}