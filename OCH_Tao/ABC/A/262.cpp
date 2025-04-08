#include <bits/stdc++.h>
using namespace std;
int main() {
  int Y;
  cin >> Y;
  cout << Y + (6 - Y % 4) % 4 << endl;
}