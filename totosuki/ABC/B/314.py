from collections import defaultdict

N = int(input())
data = defaultdict(set)
for i in range(1, N+1):
  C = int(input())
  A = set(map(int, input().split()))
  data[i] = A

X = int(input())
d1 = defaultdict(set)

for i in range(1, N+1):
  A = data[i]
  if X in A:
    d1[i] = A

rslt = defaultdict(list)

for i in d1.keys():
  length = len(d1[i])
  rslt[length].append(i)

if not rslt:
  print(0)
  exit()

min_len = min(rslt.keys())
min_len_num = len(rslt[min_len])

print(min_len_num)
print(*rslt[min_len])