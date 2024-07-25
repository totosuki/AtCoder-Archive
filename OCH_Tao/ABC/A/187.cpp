#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A = 0;
  int B = 0;
  for (int i = 0; i < 3; i++)
  {
    char X;
    cin >> X;
    A += int(X - '0');
  }
  for (int i = 0; i < 3; i++)
  {
    char X;
    cin >> X;
    B += int(X - '0');
  }
  cout << max(A, B) << endl;
}