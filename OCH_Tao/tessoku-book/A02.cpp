#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, X;
  cin >> N >> X;
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  for (int i : A) {
    if (i == X) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
}