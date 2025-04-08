#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, X;
  cin >> N;
  X = floor(N * 1.08);
  cout << (X < 206 ? "Yay!" : X == 206 ? "so-so" : ":(") << endl;
}