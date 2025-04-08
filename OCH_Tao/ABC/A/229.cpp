#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S1, S2;
  cin >> S1 >> S2;
  cout << ((S1 == ".#" && S2 == "#.") || (S1 == "#." && S2 == ".#") ? "No" : "Yes") << endl;
}