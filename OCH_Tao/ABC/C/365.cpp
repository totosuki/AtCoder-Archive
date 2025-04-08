#include <bits/stdc++.h>
using namespace std;
int main()
{
  int64_t N, M, cnt;
  cin >> N >> M;
  cnt = M / N;
  vector<int64_t> A(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
  }
  if (reduce(A.begin(), A.end()) <= M)
  {
    cout << "infinite" << endl;
  }
  else
  {
    while (true)
    {
      int64_t tmp = 0;
      for (int i = 0; i < N; i++)
      {
        tmp += min(cnt, A[i]);
      }
      if (tmp > M)
      {
        cout << cnt - 1 << endl;
        break;
      }
      else
      {
        cnt += 1;
      }
    }
  }
}