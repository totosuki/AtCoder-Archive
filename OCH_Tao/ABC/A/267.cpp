#include <bits/stdc++.h>
using namespace std;
int main() {
  string S;
  cin >> S;
  vector<string> V = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
  cout << 5 - distance(V.begin(), find(V.begin(), V.end(), S)) << endl;
}