#include <bits/stdc++.h>
using namespace std;

int main(){
  vector<int> data(5);
  string answer = "NO";
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
  }

  for (int i = 0; i < 4; i++) {
    if (data[i] == data[i+1]) {
      answer = "YES";
    }
  }

  cout << answer << endl;
}