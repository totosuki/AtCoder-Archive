#include <bits/stdc++.h>
using namespace std;

int main(){
  int pattern;
  string text;
  int price;
  int N;
  cin >> pattern;
  if (pattern == 1) {
    cin >> price;
    cin >> N;
    cout << price * N << endl;
  }
  else if (pattern == 2) {
    cin >> text >> price >> N;
    cout << text + "!" << endl;
    cout << price * N << endl;
  }
}