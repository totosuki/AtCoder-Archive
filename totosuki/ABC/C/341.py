H, W, N = map(int, input().split())
T = list(input())
tile = [list(input()) for _ in range(H)]

# 陸のいちをまとめる
dots = []
for row in range(H):
  for col in range(W):
    if tile[row][col] == ".":
      dots.append((row, col))

rslt = set() # 移動の最終結果
vec = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)} # (y, x) の順

for dot in dots:
  y, x = dot
  for t in T:
    ny, nx = y + vec[t][0], x + vec[t][1]
    if tile[ny][nx] == "#":
      break
    else:
      y, x = ny, nx
  else:
    rslt.add((ny, nx))

print(len(rslt))