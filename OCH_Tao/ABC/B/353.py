N,K = map(int,input().split())
A = list(map(int,input().split()))
tmp = 0
cnt = 0
for i in A:
  if K-tmp<i:
    cnt+=1
    tmp = 0
  tmp+=i
else:
  cnt+=1
print(cnt)