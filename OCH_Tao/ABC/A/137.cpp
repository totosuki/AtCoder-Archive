#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  cin >> A >> B;
  cout << max({A + B, A - B, A * B}) << endl;
}