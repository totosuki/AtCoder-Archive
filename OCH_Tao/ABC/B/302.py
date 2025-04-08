import numpy as np
H, W = map(int, input().split())
S = np.array([list(input()) for _ in range(H)])
X = np.argwhere(S == "s")
D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in X:
  cnt = ""
  for x, y in D:
    for n in range(5):
      if 0 <= i[0]+x*n < H and 0 <= i[1]+y*n < W:
        cnt += S[i[0]+x*n][i[1]+y*n]
      else:
        cnt = ""
        break
    if cnt == "snuke":
      [print(i[0]+x*n+1, i[1]+y*n+1) for n in range(5)]
      exit()
    else:
      cnt = ""
