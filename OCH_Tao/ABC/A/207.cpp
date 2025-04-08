#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C;
  cin >> A >> B >> C;
  cout << A + B + C - min({A, B, C}) << endl;
}