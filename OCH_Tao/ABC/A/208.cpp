#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  cin >> A >> B;
  cout << (A <= B && B <= 6 * A ? "Yes" : "No") << endl;
}