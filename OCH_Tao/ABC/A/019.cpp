#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> vec(3);
  for (int i = 0; i < 3; i++)
  {
    cin >> vec.at(i);
  }
  sort(vec.begin(), vec.end());
  cout << vec.at(1) << endl;
}