import sys
input = sys.stdin.buffer.readline

N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

for a in range(10**6+5):
  b = 1 << 60
  for i in range(N):
    if Q[i] < a * A[i]:
      break
    elif B[i] != 0:
      b = min(b, (Q[i] - a * A[i]) // B[i])
  else:
    ans = max(ans, a + b)

print(ans)
