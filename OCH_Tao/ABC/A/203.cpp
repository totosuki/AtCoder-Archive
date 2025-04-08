#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C;
  cin >> A >> B >> C;
  cout << (A == B ? C : B == C ? A : C == A ? B : 0) << endl;
}