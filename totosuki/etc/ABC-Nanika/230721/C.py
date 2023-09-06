import sys
input = sys.stdin.buffer.readline

N, T = map(int, input().split())
A = list(map(int, input().split()))
all_time = sum(A)

T = T % all_time

for i in range(N):
  if T - A[i] < 0:
    print(i+1, T)
    break
  T -= A[i]