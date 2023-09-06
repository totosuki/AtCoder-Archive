from collections import defaultdict

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
dict = defaultdict(list)

for d in data:
  dict[d[0]].append(d[1])
  dict[d[1]].append(d[0])

dict = sorted(dict.items())
rslt = [[0] for _ in range(N)]
for k, r in dict:
  r.sort()
  tmp = [len(r), *r]
  rslt[k-1] = tmp
[print(*r) for r in rslt]