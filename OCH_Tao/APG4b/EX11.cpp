#include <bits/stdc++.h>
using namespace std;
int main()
{
  int N, A;
  cin >> N >> A;
  int i = 0;
  for (; i < N; i++)
  {
    string op;
    int B;
    cin >> op >> B;
    if (op == "+")
    {
      A += B;
    }
    else if (op == "-")
    {
      A -= B;
    }
    else if (op == "*")
    {
      A *= B;
    }
    else
    {
      if (B != 0)
      {
        A /= B;
      }
      else
      {
        cout << "error" << endl;
        break;
      }
    }
    cout << i + 1 << ":" << A << endl;
  }
}