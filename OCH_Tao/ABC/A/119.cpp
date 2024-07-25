#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  int M = stoi(S.substr(5, 2));
  cout << (M < 5 ? "Heisei" : "TBD") << endl;
}