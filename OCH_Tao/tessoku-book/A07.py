from itertools import accumulate
D = int(input())
N = int(input())
X = [0]*(D+2)
for i in range(N):
  L, R = map(int, input().split())
  X[L] += 1
  X[R+1] -= 1
[print(i) for i in list(accumulate(X))[1:-1]]
