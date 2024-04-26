#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, S, T;
  cin >> N >> S >> T;
  vector<int> W(N);
  cin >> W[0];
  for (int i = 0; i < N - 1; i++)
  {
    int A;
    cin >> A;
    W[i + 1] = W[i] + A;
  }
  int cnt = 0;
  for (int i = 0; i < N; i++)
  {
    if (S <= W[i] && W[i] <= T)
    {
      cnt++;
    }
  }
  cout << cnt << endl;
}