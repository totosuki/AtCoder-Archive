#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, Q;
  cin >> N >> Q;
  vector<int64_t> A(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
  }
  for (int i = 0; i < Q; i++)
  {
    int64_t B, K;
    cin >> B >> K;
    vector<int64_t> X(N);
    for (int i = 0; i < N; i++)
    {
      X[i] = abs(A[i] - B);
    }
    sort(X.begin(), X.end());
    cout << X[K - 1] << endl;
  }
}