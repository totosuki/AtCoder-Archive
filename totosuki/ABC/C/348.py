N = int(input())
d = {}
for _ in range(N):
  A, C = map(int, input().split())
  d[C] = min(d.get(C, 1e9), A)
print(sorted(d.values())[-1])

# 101byte
# d={}
# for s in[*open(0)][1:]:a,c=s.split();d[c]=min(d.get(c,1e9),int(a))
# print(sorted(d.values())[-1])

# 90byte
print(max(dict(sorted([*map(int,s.split()[::-1])]for s in[*open(0)][1:])[::-1]).values()))
