import sys
input = sys.stdin.buffer.readline

H, W, N = map(int, input().split())
tile = [[0]*1550 for _ in range(1550)]
cum = [[0]*1550 for _ in range(1550)]

# 前処理
for _ in range(N):
  A, B, C, D = map(int, input().split())
  tile[A][B] += 1
  tile[A][D+1] -= 1
  tile[C+1][B] -= 1
  tile[C+1][D+1] += 1

# 累積和
for y in range(1, 1550):
  for x in range(1, 1550):
    cum[y][x] = cum[y][x-1] + tile[y][x]
for x in range(1, 1550):
  for y in range(1, 1550):
    cum[y][x] += cum[y-1][x]

# 出力
for i in range(1, H+1):
  print(*cum[i][1:W+1])