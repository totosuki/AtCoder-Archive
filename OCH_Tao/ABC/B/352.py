S = list(input())
T = input()
cnt = 0
L = []
for i in S:
  X = T.index(i,cnt)+1
  L.append(X)
  cnt = X
print(*L)