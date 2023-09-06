import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
rslt = [0] * (2*N+1)

for i in range(1,N+1):
  rslt[2*i-1] = rslt[A[i-1]-1]+1
  rslt[2*i] = rslt[A[i-1]-1]+1

[print(r) for r in rslt]