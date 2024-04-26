#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A, B, Alice, Bob;
  cin >> A >> B;
  vector<int> hand = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1};
  Alice = distance(hand.begin(), find(hand.begin(), hand.end(), A));
  Bob = distance(hand.begin(), find(hand.begin(), hand.end(), B));
  if (Alice > Bob)
  {
    cout << "Alice";
  }
  else if (Alice < Bob)
  {
    cout << "Bob";
  }
  else
  {
    cout << "Draw";
  }
  cout << endl;
}