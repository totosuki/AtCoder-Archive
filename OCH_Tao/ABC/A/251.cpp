#include <bits/stdc++.h>
using namespace std;
int main() {
  string S;
  cin >> S;
  S += S;
  S += S;
  S += S;
  cout << S.substr(0, 6) << endl;
}