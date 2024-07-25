N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
cnt = 0
for i in range(N):
  cnt+=B[A[i]-1]
  if i>0:
    if A[i]-A[i-1]==1:
      cnt+=C[A[i-1]-1]
print(cnt)