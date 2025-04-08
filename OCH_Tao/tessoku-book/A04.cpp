#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  for (int i = 9; i >= 0; i--) {
    cout << N / (1 << i) % 2;
  }
  cout << endl;
}