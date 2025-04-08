N,M = map(int,input().split())
L = [True]*N
for i in range(M):
  A,B = input().split()
  A = int(A)-1
  if B=="M" and L[A]:
    print("Yes")
    L[A]=False
  else:
    print("No")