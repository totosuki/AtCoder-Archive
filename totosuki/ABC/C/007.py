import sys, collections
input = sys.stdin.buffer.readline

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
M = []
for row in range(R):
  c = input().decode().strip()
  M.append(c)
dist = [[-1]*C for _ in range(R)]
angles = [[-1, 0], [0, 1], [1, 0], [0, -1]]

dist[sy-1][sx-1] = 0
queue = collections.deque([[sy-1, sx-1]])

while len(queue):
  y, x = queue.popleft()
  
  for angle in angles:
    ny, nx = y+angle[0], x+angle[1]
    # print(f"ny: {ny}, nx: {nx}")
    if not (0 <= ny < R) or not (0 <= nx < C):
      continue
    if (M[ny][nx] != "#") and (dist[ny][nx] == -1):
      dist[ny][nx] = dist[y][x] + 1
      queue.append([ny, nx])

print(dist[gy-1][gx-1])

# while len(queue):
#   print(f"queue: {queue}")
#   pos = queue.pop()
#   print(f"pos: {pos}")
#   y = pos[0]
#   x = pos[1]
#   for angle in angles:
#     n_y = x + angle[0]
#     n_x = y + angle[1]
#     if not (0 <= n_y < R) or not (0 <= n_x < C):
#       continue
#     if (M[n_y][n_x] >= 0) and (status[n_y][n_x] == False):
#       M[n_y][n_x] = M[y][x] + 1
#       status[n_y][n_x] = True
#       queue.append([n_y, n_x])
#   print(*status, sep = "\n", end = "\n\n")