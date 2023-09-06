#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  int A;
  string op;
  int B;
  cin >> N >> A;
  for (int i = 0; i < N; i++) {
    cin >> op >> B;
    if (op == "+") {
      A += B;
    }
    else if (op == "-") {
      A -= B;
    }
    else if (op == "*") {
      A *= B;
    }
    else if (op == "/") {
      if (B == 0) {
        cout << "error" << endl;
        break;
      }
      A /= B;
    }

    cout << i+1 << ":" << A << endl;
  }
}