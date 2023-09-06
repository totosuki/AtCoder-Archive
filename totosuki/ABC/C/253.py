import sys; from collections import defaultdict; import heapq
input = sys.stdin.buffer.readline

Q = int(input())
dict = defaultdict(int)
# mx = -1
# mn = 10 ** 9 + 10
mx = []
mn = []
heapq.heapify(mx)
heapq.heapify(mn)

for _ in range(Q):
  query = list(map(int, input().split()))
  mode = query[0]
  if mode == 1:
    x = query[1]
    dict[x] += 1
    heapq.heappush(mx, -x)
    heapq.heappush(mn, x)
  elif mode == 2:
    x = query[1]
    c = query[2]
    dict[x] -= min(dict[x], c)
    if dict[x] == 0:
      del dict[x]
  elif mode == 3:
    mx_pop = 0
    mn_pop = 0
    while True:
      a = heapq.heappop(mx)
      a = -a
      if dict[a] > 0:
        heapq.heappush(mx, -a)
        mx_pop = a
        break
    while True:
      a = heapq.heappop(mn)
      if dict[a] > 0:
        mn_pop = a
        heapq.heappush(mn, a)
        break
    print(mx_pop - mn_pop)