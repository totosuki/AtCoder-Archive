#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cin >> N;
  cout << (N < 126 ? 4 : N < 212 ? 6 : 8) << endl;
}