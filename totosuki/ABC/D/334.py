from bisect import bisect_right

N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
cum = [0] * (N+1)
for i in range(1, N+1):
  cum[i] = cum[i-1] + R[i-1]


for _ in range(Q):
  X = int(input())
  left = bisect_right(cum, X)
  print(left-1)