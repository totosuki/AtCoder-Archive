import sympy.ntheory as sym
N = int(input())
cnt = 0
for i in range(1,N+1,2):
  D = sym.factorint(i)
  x = 1
  for j in D.values():
    x*=j+1
  if x==8:
    cnt+=1
print(cnt)