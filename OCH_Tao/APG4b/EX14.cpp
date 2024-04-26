#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, C;
  cin >> A >> B >> C;
  int highest = max(max(A, B), C);
  int shortest = min(min(A, B), C);
  cout << highest - shortest << endl;
}