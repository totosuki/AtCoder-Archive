from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
tile = [["_" for _  in range(C+1)]] + [["_"] + list(input()) for _ in range(R)]

vec = [(1,0),(-1,0),(0,1),(0,-1)]
que = deque()
que.append((sy, sx))
ans = [[-1] * (C+1) for _ in range(R+1)]
ans[sy][sx] = 0

while que:
  y, x = que.pop()
  for vy, vx in vec:
    ny = y + vy
    nx = x + vx
    if ans[ny][nx] == -1 and tile[ny][nx] == ".":
      que.appendleft((ny, nx))
      ans[ny][nx] = ans[y][x] + 1

print(ans[gy][gx])