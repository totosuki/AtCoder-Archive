import sys
input = sys.stdin.buffer.readline

N, A, B = map(int, input().split())
tile = []

for i in range(N):
  for j in range(A):
    S = ""
    flag = bool()
    if i % 2 == 0:
      flag = True
    else:
      flag = False
    for k in range(N):
      for l in range(B):
        if k % 2 == 0 and flag:
          S += "."
        elif k % 2 == 1 and not flag:
          S += "."
        elif k % 2 == 1 and flag:
          S += "#"
        elif k % 2 == 0 and not flag:
          S += "#"
    tile.append(S)

print(*tile, sep = "\n")