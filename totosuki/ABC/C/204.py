import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
  A, B = map(int, input().split())
  G[A].append(B)

rslt = [1] * (N+1)
rslt[0] = 0

def dfs(now, seen):
  seen[now] = True
  for next in G[now]:
    if not seen[next]:
      rslt[next] += 1
      dfs(next, seen)

for i in range(1, N+1):
  seen = [False] * (N+1)
  dfs(i, seen)

print(sum(rslt))