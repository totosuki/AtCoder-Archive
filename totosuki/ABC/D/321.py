import sys
input = sys.stdin.buffer.readline

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
rslt = 0
cum = [0] * (M+1)

for i in range(1, M+1):
  cum[i] = cum[i-1] + B[i-1]

def binary_search(Ai: int): # Pより大きい最小のA+Bの番号を返す
  left = -1
  right = M
  
  while right - left > 1:
    mid = (left + right) // 2
    
    if Ai + B[mid] <= P:
      left = mid
    else:
      right = mid
  
  return right

for i in range(N):
  pos = binary_search(A[i])
  rslt += (cum[pos] + (A[i] * pos)) + ((M - pos) * P)

print(rslt)