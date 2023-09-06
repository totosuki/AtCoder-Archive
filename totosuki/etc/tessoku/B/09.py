import sys
input = sys.stdin.buffer.readline

N = int(input())
tile = [[0]*1505 for _ in range(1505)]
cum = [[0]*1505 for _ in range(1505)]
cnt = 0

for _ in range(N):
  A, B, C, D = map(int, input().split())
  A, B, C, D = map(lambda x: x+1, [A, B, C, D])
  tile[A][B] += 1
  tile[C][D] += 1
  tile[A][D] -= 1
  tile[C][B] -= 1

# 累積和
for y in range(1, 1505):
  for x in range(1, 1505):
    cum[y][x] = cum[y][x-1] + tile[y][x]
for x in range(1, 1505):
  for y in range(1, 1505):
    cum[y][x] += cum[y-1][x]

for y in range(1505):
  for x in range(1505):
    if cum[y][x] > 0: cnt += 1

print(cnt)

# 座標の数値は0の可能性があるから、全て+1する必要あり