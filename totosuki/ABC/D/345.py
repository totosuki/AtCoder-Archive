from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

N, H, W = map(int, input().split())
tiles = [tuple(map(int, input().split())) for _ in range(N)]
tiles.sort(key=lambda x: x[0]*x[1], reverse=True)

# マス目を表す二次元配列を初期化
grid = [[False] * W for _ in range(H)]

# タイルの面積の合計を計算
total_area = sum(w * h for w, h in tiles)
# マス目の面積
grid_area = H * W

def check(x, y, w, h):
  if x + w > W or y + h > H:
    return False
  for i in range(y, y + h):
    for j in range(x, x + w):
      if grid[i][j]:
        return False
  return True

def place(x, y, w, h):
  for i in range(y, y + h):
    for j in range(x, x + w):
      grid[i][j] = True

def remove(x, y, w, h):
  for i in range(y, y + h):
    for j in range(x, x + w):
      grid[i][j] = False

def solve(id, covered_area=0):
  if covered_area + sum(w * h for w, h in tiles[id:]) < grid_area:
      return False
  if id == N:
    return all(all(row) for row in grid)
  # タイルを使用しない選択
  if solve(id + 1, covered_area):
    return True
  # タイルを使用する選択
  for y in range(H):
    for x in range(W):
      for w, h in [(tiles[id][0], tiles[id][1]), (tiles[id][1], tiles[id][0])]:
        if check(x, y, w, h):
          place(x, y, w, h)
          if solve(id + 1, covered_area + w * h):
            return True
          remove(x, y, w, h)
  return False

if total_area < grid_area:
  print("No")
elif solve(0):
  print("Yes")
else:
  print("No")