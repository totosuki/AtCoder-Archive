#include <bits/stdc++.h>
using namespace std;

int main(){
  string S;
  cin >> S;

  int x = 1;
  int i = 0;
  for (int i = 1; i < S.length(); i += 2) {
    if (S.at(i) == '+') {
      x++;
    }
    else if (S.at(i) == '-') {
      x--;
    }
  }

  cout << x << endl;
}