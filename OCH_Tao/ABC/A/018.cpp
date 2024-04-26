#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<int> vec(3);
  for (int i = 0; i < 3; i++)
  {
    cin >> vec.at(i);
  }
  vector<int> ABC = vec;
  sort(ABC.begin(), ABC.end());
  reverse(ABC.begin(), ABC.end());
  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      if (vec.at(i) == ABC.at(j))
      {
        cout << j + 1 << endl;
      }
    }
  }
}