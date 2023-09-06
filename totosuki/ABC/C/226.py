import sys; from collections import defaultdict, deque
input = sys.stdin.buffer.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
T_l = [0] * N
graph = defaultdict(list)
rslt = 0

for i in range(N):
  T_l[i] = data[i][0]
  graph[i+1] = data[i][2:]

# DFS
q = deque()
q.append(N)
check = [False] * N
check[N-1] = True
rslt += T_l[N-1]

while len(q):
  now = q.pop()
  next = graph[now]
  
  for n in next:
    if not check[n-1]:
      rslt += T_l[n-1]
      q.append(n)
      check[n-1] = True

print(rslt)