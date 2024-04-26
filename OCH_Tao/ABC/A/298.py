import collections
N = int(input())
S = collections.Counter(input())
if S.get("x",0)==0 and S.get("o",0)>=1:
  print("Yes")
else:
  print("No")