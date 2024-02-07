N,M = map(int,input().split())
l = []
for i in range(M):
  a,b = map(int,input().split())
  l.append(a)
  l.append(b)
for i in range(1,N+1):
  print(l.count(i))