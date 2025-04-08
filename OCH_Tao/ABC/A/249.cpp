#include <bits/stdc++.h>
using namespace std;
int main() {
  int A, B, C, D, E, F, X;
  cin >> A >> B >> C >> D >> E >> F >> X;
  int Tak = 0;
  int Aok = 0;
  for (int i = 0; i < X; i++) {
    if (i % (A + C) < A) {
      Tak += B;
    }
    if (i % (D + F) < D) {
      Aok += E;
    }
  }
  cout << (Tak > Aok ? "Takahashi" : Tak < Aok ? "Aoki" : "Draw") << endl;
}