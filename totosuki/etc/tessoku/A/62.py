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

def dfs(k):
  seen[k] = True
  for next in G[k]:
    if not seen[next]:
      dfs(next)
  return

dfs(1)

if False in seen:
  print("The graph is not connected.")
else:
  print("The graph is connected.")