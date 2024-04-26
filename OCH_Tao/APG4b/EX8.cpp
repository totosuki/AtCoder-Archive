#include <bits/stdc++.h>
using namespace std;

int main()
{
  int p;
  cin >> p;
  if (p == 2)
  {
    string text;
    cin >> text;
    cout << text << "!" << endl;
  }
  int price, N;
  cin >> price >> N;
  cout << price * N << endl;
}