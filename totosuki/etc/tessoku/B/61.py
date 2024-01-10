from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
  A, B = map(int, input().split())
  G[A].append(B)
  G[B].append(A)

mx = -1
ans = -1

for k, v in G.items():
  x = len(v)
  if x > mx:
    ans = k
    mx = x

print(ans)