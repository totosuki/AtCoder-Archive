from itertools import accumulate
T = int(input())
N = int(input())
X = [0]*(T+1)
for i in range(N):
  L, R = map(int, input().split())
  X[L] += 1
  X[R] -= 1
ans = list(accumulate([0]+X))[1:]
[print(ans[i]) for i in range(T)]
