#include <bits/stdc++.h>
using namespace std;

int main(){
  int A, B;
  cin >> A >> B;

  int i = 0;

  string text = "A:";
  while (i < A) {
    text += "]";
    i++;
  }
  cout << text << endl;

  i = 0;
  text = "B:";
  while (i < B) {
    text += "]";
    i++;
  }
  cout << text << endl;
}