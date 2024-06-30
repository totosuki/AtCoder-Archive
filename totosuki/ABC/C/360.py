from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

ans = 0
d = defaultdict(list)

for i in range(N):
  d[A[i]].append(W[i])

for k in d.keys():
  if len(d[k]) > 1:
    ans += sum(d[k]) - max(d[k])

print(ans)