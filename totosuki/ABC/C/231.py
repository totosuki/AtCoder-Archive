import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def binary_search(x):
  left = -1
  right = N

  while right - left > 1:
    mid = (left + right ) // 2
    if A[mid] < x: left = mid
    else: right = mid
  
  return right

for _ in range(Q):
  x = int(input())
  rslt = binary_search(x)
  print(N - rslt)