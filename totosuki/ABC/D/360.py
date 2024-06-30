from bisect import bisect_left, bisect_right

N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

plus = []
minus = []

for i in range(N):
  if S[i] == "0":
    minus.append(X[i] )
  else:
    plus.append(X[i] )

plus.sort()
minus.sort()

ans = 0

for x in plus:
  before_id = bisect_left(minus, x)
  end_id = bisect_right(minus, x + T*2)
  ans += end_id - before_id

print(ans)