#include <bits/stdc++.h>
using namespace std;

int main(){
  vector<int> ABC(3);
  cin >> ABC.at(0) >> ABC.at(1) >> ABC.at(2);
  sort(ABC.begin(), ABC.end());
  cout << ABC.at(2) - ABC.at(0) << endl;
}