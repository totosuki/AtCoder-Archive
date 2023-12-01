H, W = map(int, input().split())
tile = [list(input()) for _ in range(H)]
answer = -1

def return_cnt(row, col):
  cnt = 0
  vec = [[1,0],[0,1],[-1,0],[0,-1]]
  for v in vec:
    py, px = row, col
    while (0 <= py < H) and (0 <= px < W) and (tile[py][px] != "#"):
      cnt += 1
      py += v[0]
      px += v[1]
  return cnt - 3

for row in range(H):
  for col in range(W):
    if tile[row][col] == "#": continue
    answer = max(return_cnt(row, col), answer)

print(answer)