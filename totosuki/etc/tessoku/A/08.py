import sys
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
cum = [[0]*(W+1) for _ in range(H+1)]

# 横方向
for y in range(1, H+1):
  for x in range(1, W+1):
    cum[y][x] = cum[y][x-1] + X[y-1][x-1]
# 縦方向
for x in range(1, W+1):
  for y in range(1, H+1):
    cum[y][x] += cum[y-1][x]

Q = int(input())

for _ in range(Q):
  A, B, C, D = map(int, input().split())
  x = cum[C][D]
  y = cum[A-1][D] + cum[C][B-1]
  z = cum[A-1][B-1]
  print(x - y + z)