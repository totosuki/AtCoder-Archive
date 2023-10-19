from collections import deque, defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

ok = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
  isok = ok[i]
  if isok == False: # まだ頂点を通っていないならBFS
    cnt += 1
    ok[i] = True
    q = deque()
    q.append(i)
    while len(q):
      now = q.pop()
      next = graph[now]
      
      for n in next:
        if ok[n] == False:
          q.appendleft(n)
          ok[n] = True

print(cnt)