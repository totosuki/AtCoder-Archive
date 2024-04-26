import re
A,B = map(int,input().split())
X = re.compile(bin(min(A,B))+"[01]{1}")
if re.fullmatch(X,bin(max(A,B))):
  print("Yes")
else:
  print("No")