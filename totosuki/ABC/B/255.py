import sys, math
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(N)]
A_data = [d for i, d in enumerate(data) if (i+1) in A]
dist_list = list()

for i in range(1, N+1):
  if i in A:
    continue
  else:
    min_dist = 10**10
    x1, y1 = data[i-1][0], data[i-1][1]

    for d in A_data:
      x2, y2 = d[0], d[1]
      dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
      min_dist = min(min_dist, dist)
    
    dist_list.append(min_dist)

print(max(dist_list))