import sys; from collections import deque
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
tile = list()
for i in range(N):
  S = input().decode().strip()
  tmp = list()
  for s in S:
    if s == "#": tmp.append(-1)
    else: tmp.append(1000)
  tile.append(tmp)
angles = [[-1, 0], [0, 1], [1, 0], [0, -1]]

tile[1][1] = 1
queue = deque([[1, 1]])
stop_cnt = 1

while len(queue):
  y, x = queue.popleft()

  for angle in angles:
    ny, nx = y+angle[0], x+angle[1]

    if tile[ny][nx] == -1: continue

    while True:
      if tile[ny+angle[0]][nx+angle[1]] != -1:
        ny, nx = ny+angle[0], nx+angle[1]
        if tile[ny][nx] == 1000:
          stop_cnt += 1
          tile[ny][nx] = 1
      else:
        break

    if tile[ny][nx] == 1000 or tile[ny][nx] == 1:
      tile[ny][nx] = 0
      if tile[ny][nx] == 1000:
        stop_cnt += 1
      queue.append([ny, nx])

print(stop_cnt)