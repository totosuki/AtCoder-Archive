from collections import deque, defaultdict

H, W = map(int, input().split())
tile = [list(input()) for _ in range(H)]
N = int(input())
medicine = defaultdict(int)

for i in range(N):
  R, C, E = map(int, input().split())
  medicine[(R-1, C-1)] = E

start = ()
goal = ()
for i in range(H):
  for j in range(W):
    if tile[i][j] == "S":
      start = (i, j)
    elif tile[i][j] == "T":
      goal = (i, j)


seen = [[-1]*W for _ in range(H)]
seen[start[0]][start[1]] = 0
queue = deque([(start, 0)]) # (pos, cost)
ans = "No"

while len(queue):
  pos, point = queue.pop()
  
  # 薬があり、薬よりポイントが低い場合
  if medicine[pos] and point < medicine[pos]:
    point = medicine[pos]
  # ゴールの場合
  if pos == goal:
    ans = "Yes"
    break
  
  point -= 1
  if point < 0: # ポイントが0以下の場合
    continue
  
  # 4方向に移動
  for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    x, y = pos[0]+dx, pos[1]+dy
    # 範囲外や壁の場合
    if x < 0 or x >= H or y < 0 or y >= W or tile[x][y] == "#":
      continue
    # 訪れてないか、前に訪れたときよりポイントが高い場合は更新
    if seen[x][y] == -1 or seen[x][y] < point:
      seen[x][y] = point
      queue.appendleft(((x, y), point))

print(ans)