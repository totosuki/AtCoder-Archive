#include <bits/stdc++.h>
using namespace std;
int main()
{
  string N;
  cin >> N;
  for (int i = 0; i < 3; i++)
  {
    cout << (N[i] == '1' ? "9" : "1");
  }
  cout << endl;
}