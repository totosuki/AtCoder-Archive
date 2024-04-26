import collections
X = list(map(int,input().split()))
C = collections.Counter(X)
L = list(C.values())
if L.count(2)==1 and L.count(3)==1:
  print("Yes")
else:
  print("No")