import collections

N = int(input())
A = list(map(int, input().split()))
dict = collections.defaultdict(int)
rslt = 0

for a in A:
  dict[a] += 1

for cnt in dict.values():
  rslt += cnt // 2

print(rslt)