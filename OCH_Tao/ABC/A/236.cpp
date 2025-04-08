#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  int A, B;
  cin >> S >> A >> B;
  swap(S[A - 1], S[B - 1]);
  cout << S << endl;
}