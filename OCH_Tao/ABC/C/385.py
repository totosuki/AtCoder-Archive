from itertools import groupby
N = int(input())
H = list(map(int, input().split()))
ans = 1
for i in range(1, N//2+1):
  for j in range(i):
    X = H[j::i]
    for k in [len(list(a)) for _, a in groupby(X)]:
      ans = max(ans, k)
print(ans)
