from collections import deque

H, W = map(int, input().split())
tile = [list(input()) for _ in range(H)]

seen = [[False] * W for _ in range(H)]
vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = [[0] * W for _ in range(H)]

def solve(i, j):
  q = deque([(i, j)])
  this_time_seen = set()
  went = []
  cnt = 0
  while len(q):
    y, x = q.pop()
    
    if (y, x) in this_time_seen:
      continue
    
    this_time_seen.add((y, x))
    went.append((y, x))
    flag = False
    cnt += 1
    # 今の自分の周りに磁石はあるか？
    for v in vec:
      dy, dx = v
      ny, nx = y + dy, x + dx
      if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
      if tile[ny][nx] == '#':
        flag = True
        break
    # 磁石があったら終了
    if flag:continue
    
    # 磁石が無い場合、周りを探索
    for v in vec:
      dy, dx = v
      ny, nx = y + dy, x + dx
      if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
      q.appendleft((ny, nx))
  # 探索後、カウントを記録
  for y, x in went:
    ans[y][x] = max(ans[y][x], cnt)
    seen[y][x] = True

for i in range(H):
  for j in range(W):
    # 磁石の場合はスキップ
    if tile[i][j] == '#': seen[i][j] = True
    if seen[i][j]: continue
    solve(i, j)

rslt = -1

for i in range(H):
  for j in range(W):
    rslt = max(rslt, ans[i][j])

print(rslt)