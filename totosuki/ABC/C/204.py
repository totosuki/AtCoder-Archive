from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
  A, B = map(int, input().split())
  G[A].append(B)

rslt = [1] * (N+1)
rslt[0] = 0

for i in range(1, N+1):
  q = deque()
  q.appendleft(i)
  seen = [False] * (N+1)
  seen[i] = True
  
  while len(q):
    now = q.pop()
    for next in G[now]:
      if not seen[next]:
        seen[next] = True
        q.appendleft(next)
        rslt[next] += 1

print(sum(rslt))