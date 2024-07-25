#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  cin >> A >> B;
  cout << ((A + B) % 2 == 0 ? to_string((A + B) / 2) : "IMPOSSIBLE") << endl;
}