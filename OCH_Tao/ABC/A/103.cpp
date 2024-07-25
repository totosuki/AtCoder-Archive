#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> A;
  for (int i = 0; i < 3; i++)
  {
    int X;
    cin >> X;
    A.push_back(X);
  }
  cout << *max_element(A.begin(), A.end()) - *min_element(A.begin(), A.end()) << endl;
}