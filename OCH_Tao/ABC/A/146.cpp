#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  vector<string> X = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
  cout << 7 - distance(X.begin(), find(X.begin(), X.end(), S)) << endl;
}