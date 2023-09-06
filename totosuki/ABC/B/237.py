import sys
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [[0] * H for _ in range(W)]

for i in range(H):
  for j in range(W):
    B[j][i] = A[i][j]

[print(*b) for b in B]