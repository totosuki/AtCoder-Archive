#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  cin >> A >> B;
  cout << (B % A == 0 ? A + B : B - A) << endl;
}