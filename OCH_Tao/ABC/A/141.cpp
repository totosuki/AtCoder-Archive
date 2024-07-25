#include <bits/stdc++.h>
using namespace std;
int main()
{
  string S;
  cin >> S;
  cout << (S == "Sunny" ? "Cloudy" : S == "Cloudy" ? "Rainy" : "Sunny") << endl;
}