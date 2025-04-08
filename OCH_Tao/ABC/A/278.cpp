#include <bits/stdc++.h>
using namespace std;
int main() {
  int N, K;
  cin >> N >> K;
  queue<int> A;
  for (int i = 0; i < N; i++) {
    int Y;
    cin >> Y;
    A.push(Y);
  }
  for (int i = 0; i < K; i++) {
    A.pop();
    A.push(0);
  }
  for (int i = 0; i < N; i++) {
    if (i < N - 1) {
      cout << A.front() << " ";
      A.pop();
    } else {
      cout << A.front() << endl;
    }
  }
}