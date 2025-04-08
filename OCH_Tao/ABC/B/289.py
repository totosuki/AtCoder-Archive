N, M = map(int, input().split())
A = set(map(int, input().split()))
L = []
tmp = 0
for i in range(1, N):
  if i not in A:
    L.extend(range(i, tmp, -1))
    tmp = i
else:
  L.extend(range(N, tmp, -1))
print(*L)
