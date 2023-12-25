#TLEで未AC
A,M,L,R = map(int,input().split())
n = []

for i in range(A,R,M):
  n.append(i)

for i in range(A,L,-M):
  n.insert(0,i)

if L == R:
  print(0)
else:
  print(len(n))