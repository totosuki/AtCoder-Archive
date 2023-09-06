import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sum([(i+1) * A[i] for i in range(M)])
B_one = sum([A[i] for i in range(M)])
rslt = B

for i in range(N-M):
  B -= B_one
  B += M * A[i+M]
  B_one -= A[i]
  B_one += A[i+M]
  rslt = max(rslt, B)

print(rslt)