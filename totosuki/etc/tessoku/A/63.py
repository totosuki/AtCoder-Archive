from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
  A, B = map(int, input().split())
  G[A].append(B)
  G[B].append(A)

que = deque([1])
seen = [False] * (N+1)
seen[1] = True
ans = [-1] * (N+1)
ans[1] = 0

while que:
  now = que.pop()
  for next in G[now]:
    if not seen[next]:
      que.appendleft(next)
      seen[next] = True
      ans[next] = ans[now] + 1

[print(ans[i]) for i in range(1, N+1)]