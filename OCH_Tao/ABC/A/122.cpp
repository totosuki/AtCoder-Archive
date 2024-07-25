#include <bits/stdc++.h>
using namespace std;
int main()
{
  char B;
  cin >> B;
  cout << (B == 'A' ? 'T' : B == 'T' ? 'A'
                        : B == 'C'   ? 'G'
                                     : 'C')
       << endl;
}