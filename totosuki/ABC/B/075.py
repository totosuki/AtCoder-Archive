H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dir = [[-1, -1],[0, -1],[1, -1],[-1, 0],[1, 0],[-1, 1],[0, 1], [1, 1]]
rslt = S

for i in range(H):
  for j in range(W):
    cnt = 0
    if S[i][j] == "#":
      continue
    
    for k in range(8):
      x = j + dir[k][1]
      y = i + dir[k][0]
      if x < 0 or W <= x or y < 0 or H <= y:
        continue
      if S[y][x] == "#":
        cnt += 1
    
    rslt[i][j] = str(cnt)

[print("".join(r)) for r in rslt]