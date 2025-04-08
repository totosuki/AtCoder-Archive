#include <bits/stdc++.h>
using namespace std;
int main() {
  set<string> st = {};
  for (int i = 0; i < 5; i++) {
    string X;
    cin >> X;
    st.insert(X);
  }
  cout << st.size() << endl;
}