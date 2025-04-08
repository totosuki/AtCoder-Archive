#include <bits/stdc++.h>
using namespace std;
int main() {
  int A, B, C;
  cin >> A >> B >> C;
  cout << ((A <= B && B <= C) || (C <= B && B <= A) ? "Yes" : "No") << endl;
}