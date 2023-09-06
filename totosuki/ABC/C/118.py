import sys
sys.setrecursionlimit(10**9)

def min_num(a, b):
  if a < b:
    return min_num(b, a)
  else:
    if a % b == 0:
      return b
    else:
      return min_num(b, a%b)

N = int(input())
A = list(map(int, input().split()))
rslt = 0

for i in range(N - 1):
  if i == 0:
    rslt = min_num(A[i], A[i+1])
  else:
    rslt = min_num(rslt, A[i+1])

print(rslt)