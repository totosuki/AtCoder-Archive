from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
dict = defaultdict(list)
indexes = []

for i in range(len(A)):
  dict[A[i]].append(i)
for i in range(1, N+1):
  tmp = dict[i]
  indexes.append(tmp[1])
indexes.sort()
rslt = [A[r] for r in indexes]
print(*rslt)