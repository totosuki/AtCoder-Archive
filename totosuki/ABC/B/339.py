

H, W, N = map(int, input().split())

tile = [list("." * W) for _ in range(H)]
vec = [[0, -1], [1, 0], [0, 1], [-1, 0]]
pos = [0, 0]
nvec = 0

for _ in range(N):
  px, py = pos
  if tile[py][px] == ".":
    tile[py][px] = "#"
    nvec = (nvec + 1) % 4
    px = (px + vec[nvec][0]) % W
    py = (py + vec[nvec][1]) % H
  else:
    tile[py][px] = "."
    nvec = (nvec - 1) % 4
    px = (px + vec[nvec][0]) % W
    py = (py + vec[nvec][1]) % H
  pos = [px, py]

[print(*tile[i], sep = "") for i in range(H)]