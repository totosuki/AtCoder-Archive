import sys; from collections import defaultdict, deque
input = sys.stdin.buffer.readline

N1, N2, M = map(int, input().split())
d1 = defaultdict(list)
d2 = defaultdict(list)

for _ in range(M):
  u, v = map(int, input().split())
  if u <= N1:
    d1[u].append(v)
    d1[v].append(u)
  else:
    d2[u].append(v)
    d2[v].append(u)

# N1 BFS
queue_1 = deque()
queue_1.appendleft(1)
ok_1 = [-1] * N1
ok_1[0] = 0

while len(queue_1):
  search = queue_1.pop()
  cnt = ok_1[search -1]
  
  next = d1[search]
  for n in next:
    n_cnt = ok_1[n-1]
    if n_cnt == -1:
      ok_1[n-1] = cnt + 1
      queue_1.appendleft(n)

# N2 BFS
queue_2 = deque()
queue_2.appendleft(N1+N2)
ok_2 = [-1] * (N1+N2)
ok_2[N1+N2-1] = 0

while len(queue_2):
  search = queue_2.pop()
  cnt = ok_2[search -1]
  
  next = d2[search]
  for n in next:
    n_cnt = ok_2[n-1]
    if n_cnt == -1:
      ok_2[n-1] = cnt + 1
      queue_2.appendleft(n)

print(max(ok_1) + max(ok_2) + 1)