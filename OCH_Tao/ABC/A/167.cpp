#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S, T;
  cin >> S >> T;
  T.pop_back();
  cout << (S == T ? "Yes" : "No") << endl;
}