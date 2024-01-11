N = int(input())

tile = [[0] * N for _ in range(N)]
tile[N//2][N//2] = "T"
tile[0][0] = 1

px = py = 0
vx = 1
vy = 0
cnt = 1
while True:
  cnt += 1

  if px + vx == N:
    vx = 0
    vy = 1
    py += 1
  elif py + vy == N:
    vx = -1
    vy = 0
    px -= 1
  elif px + vx == -1:
    vx = 0
    vy = -1
    py -= 1
  elif py + vy == -1:
    vx = 1
    vy = 0
    px += 1
  else:
    if vx == 1 and tile[py][px+1] != 0:
      vx = 0
      vy = 1
      py += 1
    elif vx == -1 and tile[py][px-1] != 0:
      vx = 0
      vy = -1
      py -= 1
    elif vy == 1 and tile[py+1][px] != 0:
      vx = -1
      vy = 0
      px -= 1
    elif vy == -1 and tile[py-1][px] != 0:
      vx = 1
      vy = 0
      px += 1
    else:
      px += vx
      py += vy
  if tile[py][px] == "T":
    break
  else:
    tile[py][px] = cnt

[print(*t) for t in tile]