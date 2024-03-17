from collections import defaultdict

N, T = map(int, input().split())

now = [0] * (N+1)
d = defaultdict(set)
for i in range(1, N+1): d[0].add(i)
rslt = {0}

for _ in range(T):
  A, B = map(int, input().split())
  next = now[A] + B
  d[now[A]].remove(A)
  d[next].add(A)
  if len(d[now[A]]) == 0:
    rslt.remove(now[A])
  if len(d[next]) == 1:
    rslt.add(next)
  now[A] = next
  print(len(rslt))