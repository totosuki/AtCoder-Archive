H,W = map(int,input().split())
A = []
for i in range(H):
  A.extend(list(map(int,input().split())))
print(sum([i-min(A) for i in A]))