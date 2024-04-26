N,M,C = map(int,input().split())
B = list(map(int,input().split()))
cnt = 0
for i in range(N):
  A = list(map(int,input().split()))
  tmp = 0
  for j in range(M):
    tmp+=A[j]*B[j]
  else:
    tmp+=C
    if tmp>0:
      cnt+=1
print(cnt)