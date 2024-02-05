import sys
input = sys.stdin.buffer.readline

N = int(input())
C = sorted(map(int, input().split()))
MOD = 10**9 + 7

ans = 1
for i in range(N):
  x = C[i] - i
  x = max(x, 0)
  ans = (ans * x) % MOD

print(ans)