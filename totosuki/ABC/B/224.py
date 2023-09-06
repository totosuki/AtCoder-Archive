import sys
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
answer = "Yes"

for i1 in range(H):
  for j1 in range(W):
    for i2 in range(i1+1, H):
      for j2 in range(j1+1, W):
        if (A[i1][j1] + A[i2][j2]) > (A[i2][j1] + A[i1][j2]):
          answer = "No"

print(answer)