N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt=0
A.sort()
B.sort()
for i in A:
  for j in range(len(B)):
    if i<B[j]:
      continue
    else:
      cnt+=B[j]
      del B[j]
print(cnt)