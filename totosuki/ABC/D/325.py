import sys
input = sys.stdin.buffer.readline

import heapq

N = int(input())
data = []

for _ in range(N):
  t, d = map(int, input().split())
  data.append((t, t+d))

data.sort(key = lambda x: x[0])

nt = data[0][0]
cnt = 0
i = 1

wait = [(data[0][1], data[0][0])]
heapq.heapify(wait)

while i < N:
  next_t, next_d = data[i]
  
  if len(wait) == 0:
    nt = next_t
  
  while next_t <= nt:
    heapq.heappush(wait, (next_d, next_t))
    i += 1
    if i < N:
      next_t, next_d = data[i]
    else:
      next_t = float("inf")
      break
  
  while len(wait):
    d, t = heapq.heappop(wait)
    
    if nt <= d:
      nt += 1
      cnt += 1

    if next_t <= nt:
      break

print(cnt)