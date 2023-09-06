import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [[0]*i for i in range(1, N+1)]

for i in range(N):
  for j in range(i+1):
    if j == 0 or j == i:
      A[i][j] = 1
    else:
      A[i][j] = A[i-1][j-1] + A[i-1][j]

[print(*a) for a in A]