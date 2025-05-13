#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, K;
  cin >> N >> K;
  vector<int> A(N), B(N), C(N), D(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  for (int i = 0; i < N; i++) {
    cin >> B[i];
  }
  for (int i = 0; i < N; i++) {
    cin >> C[i];
  }
  for (int i = 0; i < N; i++) {
    cin >> D[i];
  }
  set<int> P, Q;
  for (int i : A) {
    for (int j : B) {
      P.insert(i + j);
    }
  }
  for (int i : C) {
    for (int j : D) {
      Q.insert(i + j);
    }
  }
  for (int i : P) {
    if (Q.count(K - i)) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
}