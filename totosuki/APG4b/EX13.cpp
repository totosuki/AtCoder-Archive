#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<int> A(N);

  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
  }

  int ave = 0;
  for (int i = 0; i < N; i++) {
    ave += A.at(i);
  }
  ave /= N;

  for (int i = 0; i < N; i++) {
    if (A.at(i) >= ave) {
      cout << A.at(i) - ave << endl;
    }
    else if (A.at(i) < ave) {
      cout << ave - A.at(i) << endl;
    }
  }
}