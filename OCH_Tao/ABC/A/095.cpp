#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  cout << 700 + count(S.begin(), S.end(), 'o') * 100 << endl;
}