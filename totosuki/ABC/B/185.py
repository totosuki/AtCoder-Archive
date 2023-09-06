import sys
input = sys.stdin.buffer.readline

N, M, T = map(int, input().split())
max_N = N
answer = "Yes"

t = 0
for _ in range(M):
  A, B = map(int, input().split())
  N -= A - t
  if N <= 0:
    answer = "No"
  N += B - A
  N = min(max_N, N)
  t = B
else:
  N -= T - t
  if N <= 0:
    answer = "No"


print(answer)