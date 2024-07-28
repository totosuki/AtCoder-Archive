H, W = map(int, input().split())
ni, nj = map(int, input().split())
tile = [list(input()) for _ in range(H)]
X = list(input())

for x in X:
  if x == "L" and nj > 1 and tile[ni-1][nj-2] == ".":
    nj -= 1
  elif x == "R" and nj < W and tile[ni-1][nj] == ".":
    nj += 1
  elif x == "U" and ni > 1 and tile[ni-2][nj-1] == ".":
    ni -= 1
  elif x == "D" and ni < H and tile[ni][nj-1] == ".":
    ni += 1

print(ni, nj)