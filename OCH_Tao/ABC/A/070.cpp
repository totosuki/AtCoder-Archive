#include <bits/stdc++.h>
using namespace std;
int main()
{
  string N;
  cin >> N;
  string N_reverse = N;
  reverse(N_reverse.begin(), N_reverse.end());
  if (N == N_reverse)
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }
}