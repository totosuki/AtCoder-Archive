import re
from numpy import ndindex
RE = re.compile(r"\d")
R, C = map(int, input().split())
B = []
for i in range(R):
  B.append(list(input()))
for i, j in ndindex(R, C):
  if RE.match(B[i][j]):
    N = int(B[i][j])
    for r, c in ndindex(R, C):
      if abs(r-i)+abs(c-j) <= N and not RE.match(B[r][c]):
        B[r][c] = "."
    B[i][j] = "."
print(*["".join(i) for i in B], sep="\n")
