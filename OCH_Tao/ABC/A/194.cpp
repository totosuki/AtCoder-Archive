#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B;
  cin >> A >> B;
  cout << (15 <= A + B && 8 <= B ? 1 : 10 <= A + B && 3 <= B ? 2 : 3 <= A + B ? 3 : 4) << endl;
}