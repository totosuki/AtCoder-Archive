import sys; from collections import defaultdict, deque
input = sys.stdin.buffer.readline

N = int(input())
check_dict = defaultdict(bool)
dict = defaultdict(list)

for _ in range(N):
  A, B = map(int, input().split())
  dict[A].append(B)
  dict[B].append(A)
  check_dict[A] = True
  check_dict[B] = True

# BFS
q = deque()
q.appendleft(1)
check_dict[1] = False
rslt = 1

while len(q):
  now = q.pop()
  next = dict[now]
  
  for n in next:
    if check_dict[n]:
      rslt = max(rslt, n)
      check_dict[n] = False
      q.appendleft(n)

print(rslt)