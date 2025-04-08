N = int(input())
A = list(map(int,input().split()))
Q = int(input())
for i in range(Q):
  n,*k = map(int,input().split())
  if n==1:
    A[k[0]-1]=k[1]
  else:
    print(A[k[0]-1])