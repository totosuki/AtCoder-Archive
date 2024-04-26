#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cin >> N;
  if (N == 100)
  {
    cout << "Perfect" << endl;
  }
  else if (N >= 90)
  {
    cout << "Great" << endl;
  }
  else if (N >= 60)
  {
    cout << "Good" << endl;
  }
  else
  {
    cout << "Bad" << endl;
  }
}