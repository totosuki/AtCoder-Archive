N = int(input())
C = set()
D = dict()
for i in range(N):
  a,c = map(int,input().split())
  if str(c) not in C:
    C.add(str(c))
    D[str(c)] = a
  else:
    D[str(c)] = min(a,D[str(c)])
print(max(D.values()))