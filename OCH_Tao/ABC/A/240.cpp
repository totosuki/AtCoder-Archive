#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  cin >> A >> B;
  cout << (abs(A - B) == 1 || abs(A - B) == 9 ? "Yes" : "No") << endl;
}