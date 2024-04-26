#include <bits/stdc++.h>
using namespace std;
int main()
{
  char R, G, B;
  cin >> R >> G >> B;
  string RGB = {R, G, B};
  if (stoi(RGB) % 4 == 0)
  {
    cout << "YES" << endl;
  }
  else
  {
    cout << "NO" << endl;
  }
}