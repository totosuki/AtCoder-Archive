import sys
input = sys.stdin.buffer.readline

N = int(input())
B = [[0]*1550 for _ in range(1550)]
cum = [[0]*1550 for _ in range(1550)]
for _ in range(N):
  X, Y = map(int, input().split())
  B[X][Y] += 1

# 横方向
for y in range(1, 1550):
  for x in range(1, 1550):
    cum[y][x] = cum[y][x-1] + B[y][x]
# 縦方向
for x in range(1, 1550):
  for y in range(1, 1550):
    cum[y][x] += cum[y-1][x]

Q = int(input())
for _ in range(Q):
  a, b, c, d = map(int, input().split())
  x = cum[c][d]
  y = cum[a-1][b-1]
  z = cum[a-1][d] + cum[c][b-1]

  print(x + y - z)