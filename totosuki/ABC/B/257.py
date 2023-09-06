import sys
input = sys.stdin.buffer.readline

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
  # 操作1
  if A[l-1] == N:
    continue
  
  # 操作2
  if not A[l-1] +1 in A:
    A[l-1] += 1

print(*A)