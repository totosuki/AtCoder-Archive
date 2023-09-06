import sys
input = sys.stdin.buffer.readline

N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))

def binary_search(x):
  L = 1
  R = N
  while L <= R:
    ans = (L + R) // 2
    if x < A[ans]: R = ans - 1
    if x == A[ans]: return ans
    if x > A[ans]: L = ans + 1
  return -1

ans = binary_search(X)
print(ans)