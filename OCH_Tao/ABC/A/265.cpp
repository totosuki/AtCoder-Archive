#include <bits/stdc++.h>
using namespace std;
int main() {
  int X, Y, N;
  cin >> X >> Y >> N;
  cout << min((N / 3) * Y + (N % 3) * X, N * X) << endl;
}