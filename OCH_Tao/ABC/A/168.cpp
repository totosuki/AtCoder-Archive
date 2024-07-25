#include <bits/stdc++.h>
using namespace std;
int main()
{
  string N;
  cin >> N;
  char S = N.back();
  string hon = "24579";
  string pon = "0168";
  if (hon.find(S) != string::npos)
  {
    cout << "hon" << endl;
  }
  else if (pon.find(S) != string::npos)
  {
    cout << "pon" << endl;
  }
  else
  {
    cout << "bon" << endl;
  }
}