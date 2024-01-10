from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
  A, B = map(int, input().split())
  G[A].append(B)
  G[B].append(A)

nexts = [1]
ans = [-1] * (N+1)
ans[1] = 0
seen = [False] * (N+1)
seen[1] = True
dist = 0

while nexts:
  dist += 1
  nows = nexts.copy()
  nexts = []
  for now in nows:
    for next in G[now]:
      if not seen[next]:
        seen[next] = True
        nexts.append(next)
        ans[next] = dist

[print(ans[i]) for i in range(1, N+1)]