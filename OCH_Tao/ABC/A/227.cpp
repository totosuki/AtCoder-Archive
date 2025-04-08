#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, K, A;
  cin >> N >> K >> A;
  int ans = (K + A - 1) % N;
  cout << (ans == 0 ? N : ans) << endl;
}