#include <bits/stdc++.h>
using namespace std;
int main()
{
  vector<char> S(4);
  for (int i = 0; i < 4; i++)
  {
    cin >> S[i];
  }
  sort(S.begin(), S.end());
  cout << (S[0] == S[1] && S[1] == S[2] && S[2] == S[3] ? "No" : S[0] == S[1] && S[2] == S[3] ? "Yes" : "No") << endl;
}