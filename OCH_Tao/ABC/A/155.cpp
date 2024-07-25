#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C;
  cin >> A >> B >> C;
  cout << ((A == B && C != A) || (B == C && A != B) || (C == A && B != C) ? "Yes" : "No") << endl;
}