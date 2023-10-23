from collections import deque

H, W = map(int, input().split())

tile = [list(input()) for _ in range(H)]
check = [[False] * W for _ in range(H)]
cnt = 0

for row in range(H):
  for col in range(W):
    if check[row][col]:
      continue
    
    check[row][col] = True
    if tile[row][col] == "#": # 隣接+斜めしている#を探索
      q = deque()
      q.append((row, col))
      while len(q):
        now = q.pop()
        next = [(now[0] - 1, now[1]), (now[0] + 1, now[1]), (now[0], now[1] - 1), (now[0], now[1] + 1), (now[0] - 1, now[1] - 1), (now[0] - 1, now[1] + 1), (now[0] + 1, now[1] - 1), (now[0] + 1, now[1] + 1)]
        for n in next:
          if 0 <= n[0] < H and 0 <= n[1] < W and tile[n[0]][n[1]] == "#" and not check[n[0]][n[1]]:
            check[n[0]][n[1]] = True
            q.append(n)
      cnt += 1

print(cnt)