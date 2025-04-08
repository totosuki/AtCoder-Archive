#include <bits/stdc++.h>
using namespace std;
int main() {
  vector<int> L(5);
  for (int i = 0; i < 5; i++) {
    cin >> L[i];
  }
  sort(L.begin(), L.end());
  cout << ((L[0] == L[1] && L[2] == L[4]) || (L[0] == L[2] && L[3] == L[4]) ? "Yes" : "No") << endl;
}