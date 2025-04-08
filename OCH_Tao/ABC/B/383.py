from itertools import combinations
H, W, D = map(int, input().split())
L = []
for i in range(H):
  S = list(input())
  for j in range(W):
    if S[j] == ".":
      L.append((i, j))
ans = 0
for i, j in combinations(L, 2):
  cnt = 0
  for x in L:
    if abs(x[0]-i[0])+abs(x[1]-i[1]) <= D or abs(x[0]-j[0])+abs(x[1]-j[1]) <= D:
      cnt += 1
  ans = max(ans, cnt)
print(ans)
