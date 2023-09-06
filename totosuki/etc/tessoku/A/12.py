import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

def check(x):
  sm = 0
  for i in range(1, N+1): sm += x // A[i]
  if sm >= K: return True
  else: return False

L = 1
R = 10**9

while L < R:
  M = (L + R) // 2
  ans = check(M)
  if ans == False: L = M + 1
  if ans == True: R = M

print(L)