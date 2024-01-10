import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
  A, B = map(int, input().split())
  G[A].append(B)
  G[B].append(A)

seen = [False] * (N+1)
seen[0] = True
route = [N]

def dfs(now):
  seen[now] = True
  if now == N:
    return N
  for next in G[now]:
    if not seen[next]:
      if dfs(next) == N:
        route.append(now)
        return N
  return

dfs(1)
route.reverse()
print(*route)