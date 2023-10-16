import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

sm = sum(A)
div = sm // N
mod = sm % div

rslt = 0

for i in range(N):
  if i < mod:
    rslt += abs(A[i] - (div + 1))
  else:
    rslt += abs(A[i] - div)

print(rslt // 2)