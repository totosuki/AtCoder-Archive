N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
rslt = 0

dict = dict()
for d,p in zip(["a", "b", "c"], [1, 2, 3]):
  dict[d] = p

print(dict)

for c in C:
  flag = False
  for i, d in enumerate(D):
    if c == d:
      flag = True
      rslt += P[i+1]
  if not flag:
    rslt += P[0]

print(rslt)